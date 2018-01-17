from django.shortcuts import render


def index(request):
    return render(request, 'trade/index_home.html')
