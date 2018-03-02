from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist as DoesNotExistException
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .. import email
from ..models import OneshirtUser as OSUser, FRCTeam, PasswordResetRequest


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


def forgot(request):
    if request.method == 'GET':
        return render(request, 'trade/auth_forgot_pass.html')
    else:
        data = request.POST

        if 'email' in data:
            osu = get_object_or_404(OSUser, email=data['email'])
            prr = PasswordResetRequest()
            prr.user = osu
            prr.save()

            try:
                email.pass_reset_mail(prr.user, prr.key)
            except Exception as e:
                print(e)
        else:
            return HttpResponse(status=400)


def reset(request):
    if request.method == 'GET':
        if 'key' in request.GET:
            prr = get_object_or_404(PasswordResetRequest, key=request.GET['key'])
            if prr.valid:
                ctx = {}
                ctx['user'] = prr.user
                ctx['key'] = prr.key
                return render(request, 'trade/auth_reset_pass.html', ctx)
            else:
                return HttpResponse(status=403)
        else:
            return HttpResponse(status=400)
    else:
        data = request.POST
        if 'password' in data and 'key' in data:
            prr = get_object_or_404(PasswordResetRequest, key=data['key'])
            if prr and prr.valid:
                prr.user.django_user.set_password(data['password'])
                prr.user.django_user.save()
                prr.valid = False
                prr.save()

                ctx = {}
                ctx['title'] = "Password Reset Successful"
                ctx['message'] = "%s, you've successfully reset your password. You can log in with the username %s " \
                                 "and your new password using the button above. " % (
                                     prr.user.fname, prr.user.django_user.username
                                 )

                return render(request, 'trade/message.html', ctx)
            else:
                ctx = {}
                ctx['title'] = "Link Expired"
                ctx['message'] = "It looks like that link has expired. Please request a new one on the login page. "

                return render(request, 'trade/message.html', ctx)


def logout(request):
    do_logout(request)
    return redirect('trade:index')
