from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist as DoesNotExistException
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ..models import OneshirtUser as OSUser, FRCTeam


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        u = authenticate(request, username=username, password=password)
        if u:
            do_login(request, u)
            return redirect('trade:index')
        else:
            ctx = {"title": "Invalid Username/Password",
                   "message": "There was a problem logging you in. Please try again."}
            return render(request, "trade/message.html", ctx)
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

        if len(User.objects.filter(username=data['username'])) > 0:
            ctx = {}
            ctx['title'] = "Username Taken"
            ctx['message'] = "It looks like we already have a user with that username. Please select another."
            return render(request, 'trade/message.html', ctx)

        try:
            u = User.objects.create_user(data['username'], data['email'], data['password'])
            u.save()
        except ValueError:
            return HttpResponse(status=400)

        try:
            team = FRCTeam.objects.filter(number=data['team']).first()
        except DoesNotExistException:
            team = None

        osu = OSUser(django_user=u, fname=data['fname'], email=data['email'],
                     team=team)
        osu.save()

        ctx = {}
        ctx['title'] = "Successfully Created"
        ctx['message'] = "Your account has been successfully created! Log in using the navbar and list your first item!"

        return render(request, "trade/message.html", ctx)


def logout(request):
    do_logout(request)
    return redirect('trade:index')
