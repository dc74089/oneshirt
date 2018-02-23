from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from ..models import Item, Trade, OneshirtUser


def new_trade(request):
    if request.method == 'POST':
        data = request.POST

        t = Trade()
        t.requester = get_object_or_404(OneshirtUser, django_user=request.user)
        t.recipient = get_object_or_404(OneshirtUser, django_user__username=data['item_owner'])
        t.give = (get_object_or_404(Item, id=data['give']))
        t.take = (get_object_or_404(Item, id=data['take']))
        t.save()

        return redirect('trade:item_view', id=data['take'])  # TODO: Display a success message?


@csrf_exempt
def accept(request):
    if request.method == 'POST':
        t = get_object_or_404(Trade, id=request.POST['id'])
        t.status = 'a'
        t.give.available = False
        t.take.available = False

        t.give.save()
        t.take.save()
        t.save()

        return JsonResponse({"success": True})

    return JsonResponse({}, status=400)
