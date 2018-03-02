from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .. import email
from ..models import Trade, Item


def home(request):
    if not request.user.is_staff:
        return HttpResponse(status=400)

    ctx = {}
    cards = []

    for item in Item.objects.filter(verified=False).order_by('?')[:20]:
        cards.append(render_to_string("trade/partial/item_card.html", {"item": item}))

    ctx['cards'] = cards

    return render(request, 'trade/index_home.html', ctx)


def verify(request, id):
    if request.user.is_staff:
        i = get_object_or_404(Item, id=id)
        i.verified = True
        i.save()

    return redirect('trade:admin_home')


def delete(request, id):
    if request.user.is_staff:
        i = get_object_or_404(Item, id=id)
        i.delete()

    return redirect('trade:admin_home')


def feedback(request):
    if not request.method == 'POST':
        return HttpResponse(status=400)

    try:
        email.feedback_mail(request.POST.get('message'), request.user)
    except Exception as e:
        print(e)

    return redirect('trade:index')


def test(request):
    ctx = {'trade': Trade.objects.get(id=2)}
    return render(request, 'trade/email/trade_accepted.html', ctx)
