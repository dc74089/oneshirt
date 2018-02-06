from django.shortcuts import render
from django.template.loader import render_to_string

from ..models import Item


def index(request):
    ctx = {}
    cards = []

    for item in Item.objects.all().order_by('?')[:20]:
        cards.append(render_to_string("trade/partial/item_card.html", {"item": item}))

    ctx['cards'] = cards

    return render(request, 'trade/index_home.html', ctx)
