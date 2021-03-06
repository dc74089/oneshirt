from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .. import email, utils
from ..models import Item, OneshirtUser, Trade, FRCComp


def view(request, id):
    ctx = {}
    i = get_object_or_404(Item, id=id)

    if request.user.is_authenticated:
        ctx['items'] = Item.objects.filter(owner__django_user=request.user)

    if request.user.is_authenticated and request.user == i.owner.django_user:
        requests = Trade.objects.filter(take__id=i.id).exclude(status="d")
        ctx['requests'] = requests

    if request.user.is_authenticated and request.user != i.owner.django_user:
        ctx['trade_active'] = Trade.objects.filter(take__id=i.id, requester__django_user=request.user)

    if i.owner.team:
        ctx['events'] = utils.list_with_and(list(FRCComp.objects.filter(teams=i.owner.team)))

    ctx['item'] = i

    return render(request, 'trade/item_view.html', ctx)


def new(request):
    if request.method == 'GET':
        ctx = {}
        ctx['types'] = Item.item_types

        return render(request, 'trade/item_add.html', ctx)
    else:
        data = request.POST
        if not ('photo' in request.FILES and 'team' in data and 'type' in data):
            # assert False
            return HttpResponse(status=400)

        if request.FILES['photo'].size > 5500000:
            ctx = {}
            ctx['title'] = "File too large"
            ctx['message'] = "Please make sure that the photo you upload is less than 5mb in size."
            return render(request, 'trade/message.html')

        osu = get_object_or_404(OneshirtUser, django_user=request.user)
        i = Item()
        i.owner = osu
        i.team = data['team']
        if data.get('year'):
            i.year = data.get('year')
        i.classification = data['type']
        i.description = data.get('description')
        i.photo = request.FILES['photo']
        i.save()

        return redirect('trade:item_view', id=i.id)


def relist(request, id):
    i = get_object_or_404(Item, id=id)

    if not (i.owner.django_user == request.user or request.user.is_staff):
        return HttpResponse(status=401)

    i.available = True
    i.save()

    for t in Trade.objects.filter(take=i, status='a'):
        t.status = 'c'
        t.save()

        try:
            email.trade_cancelled_by_taker(t)
        except Exception as e:
            print(e)

    for t in Trade.objects.filter(give=i, status='a'):
        t.status = 'c'
        t.save()

        try:
            email.trade_cancelled_by_giver(t)
        except Exception as e:
            print(e)

    return redirect('trade:item_view', id=id)
