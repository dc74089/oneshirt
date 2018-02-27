from django.shortcuts import render

from ..models import Trade


def home(request):
    pass


def test(request):
    ctx = {'trade': Trade.objects.get(id=2)}
    return render(request, 'trade/email/trade_accepted.html', ctx)
