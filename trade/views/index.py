from django.shortcuts import render
from django.template.loader import render_to_string

from ..models import Item


def index(request):
    ctx = {}
    cards = []

    for item in Item.objects.filter(available=True).filter(verified=True).order_by('?')[:20]:
        cards.append(render_to_string("trade/partial/item_card.html", {"item": item}))

    ctx['cards'] = cards
    ctx['page'] = "index"

    return render(request, 'trade/index_home.html', ctx)


def mine(request):
    ctx = {}
    cards = []

    for item in Item.objects.filter(owner__django_user=request.user):
        cards.append(render_to_string("trade/partial/item_card.html", {"item": item}))

    ctx['cards'] = cards
    ctx['page'] = mine

    return render(request, 'trade/index_home.html', ctx)
