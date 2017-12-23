from django.shortcuts import render

def login(request):
    if request.method == 'GET':
        return render(request, 'trade/auth_login.html')
