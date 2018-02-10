from django.shortcuts import render

from ..models import Item


def search(request):
    ctx = {}
    ctx['item_types'] = Item.item_types

    return render(request, 'trade/search.html', ctx)
