from django.shortcuts import get_object_or_404, redirect

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
