from django.shortcuts import render

from ..models import Item

def view(request):
    pass

def new(request):
    ctx = {}
    ctx['types'] = Item.item_types

    return render(request, 'trade/item_add.html', ctx)
