from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from ..models import Item, OneshirtUser

def view(request, id):
    ctx = {}
    ctx['item'] = get_object_or_404(Item, id=id)


    return render(request, 'trade/item_view.html', ctx)

def new(request):
    if request.method == 'GET':
        ctx = {}
        ctx['types'] = Item.item_types

        return render(request, 'trade/item_add.html', ctx)
    else:
        data = request.POST
        if not ('photo' in request.FILES and 'team' in data and 'type' in data):
            assert False
            return HttpResponse(status=400)

        osu = get_object_or_404(OneshirtUser, django_user=request.user)
        i = Item()
        i.owner = osu
        i.team = data['team']
        i.year = data.get('year')
        i.classification = data['type']
        i.description = data.get('description')
        i.photo = request.FILES['photo']
        i.save()

        return redirect('trade:item_view', id=i.id)
