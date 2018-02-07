from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Item, OneshirtUser, Trade


def view(request, id):
    ctx = {}
    i = get_object_or_404(Item, id=id)

    if request.user.is_authenticated:
        ctx['items'] = Item.objects.filter(owner__django_user=request.user)

    if request.user.is_authenticated and request.user == i.owner.django_user:
        requests = Trade.objects.filter(take__id=i.id)
        ctx['requests'] = requests

    if request.user.is_authenticated and request.user != i.owner.django_user:
        ctx['trade_active'] = Trade.objects.filter(take__id=i.id, requester__django_user=request.user)

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

        # TODO: ???

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
