from django.shortcuts import render, redirect
from django.http import HttpResponse


def login(request):
    if request.method == 'POST':
        pass
    else:
        return HttpResponse(status=400)


def register(request):
    if request.method == 'GET':
        return render(request, "trade/auth_register.html")


def logout(request):
    return redirect('trade:index')
