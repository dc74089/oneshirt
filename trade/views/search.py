from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from ..models import Item


def search(request):
    ctx = {}
    ctx['item_types'] = Item.item_types

    return render(request, 'trade/search.html', ctx)


def do_search(request):
    if request.method == "GET":
        q = Q()

        if request.GET.get('team'):
            q = q & Q(team=request.GET['team'])
        if request.GET.get('type') != 'any':
            q = q & Q(type=request.GET['type'])
        # TODO: Event limiting

        items = Item.objects.filter(q)

        out = {"items": []}
        for item in items:
            ctx = {"item": item}
            out['items'].append(render_to_string("trade/partial/item_card.html", ctx, request))

        return JsonResponse(out)
