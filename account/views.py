from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .decorators import is_employee,is_client

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_employee:
                return redirect('emp')
            else:
                return HttpResponse('Invalid User')
        else:
            return HttpResponse('Invalid User')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login');  

@is_employee
def emp(request):
    return HttpResponse('emp')

@is_client
def client(request):
    return HttpResponse('client')
