from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from ..email import trade_mail, trade_accepted_mail
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

        trade_mail(t)

        return redirect('trade:item_view', id=data['take'])


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

        trade_accepted_mail(t)

        return JsonResponse({"success": True})

    return JsonResponse({}, status=400)
