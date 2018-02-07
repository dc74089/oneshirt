from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ..models import OneshirtUser as OSUser


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        u = authenticate(request, username=username, password=password)
        if u:
            do_login(request, u)
            return redirect('trade:index')
        else:
            # TODO: Show error message
            pass
    else:
        return HttpResponse(status=400)


def register(request):
    if request.method == 'GET':
        return render(request, "trade/auth_register.html")
    else:
        data = request.POST
        if not ('username' in data and 'password' in data and 'email' in data
                and 'team' in data and 'fname' in data):
            return HttpResponse(status=400)

        try:
            u = User.objects.create_user(data['username'], data['email'], data['password'])
            u.save()
        except ValueError:
            return HttpResponse(status=400)

        osu = OSUser(django_user=u, fname=data['fname'], email=data['email'],
                     team=data['team'])
        osu.save()

        # TODO: Logged In message with redirect
        return redirect('trade:index')


def logout(request):
    do_logout(request)
    return redirect('trade:index')
