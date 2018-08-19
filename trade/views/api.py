from django.http import JsonResponse
from django.db.models import Q

from ..models import Item


def all_items(request):
    resp = []

    for item in Item.objects.filter(verified=True):
        resp.append({
            'name': str(item),
            'team': item.team,
            'description': item.description,
            'type': item.get_classification_display(),
            'id': item.id,
            'photo': item.photo.url,
        })

    return JsonResponse({'items': resp})


def search(request):
    resp = []
    data = request.GET

    q = Q(verified=True)
    if 'team' in request.GET:
        q &= Q(team=int(data['team']))
    if 'year' in request.GET:
        q &= Q(year=int(data['year']))

    for item in Item.objects.filter(q):
        resp.append({
            'name': str(item),
            'team': item.team,
            'description': item.description,
            'type': item.get_classification_display(),
            'id': item.id,
            'photo': item.photo.url,
        })

    return JsonResponse(resp)
