from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from .models import profile
from speedyapp1.models import *
# Create your views here.


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_obj = User.objects.filter(username=username)
        if not user_obj.exists:
            messages.error(request,'User doesnot exists')
            return HttpResponseRedirect(request.path_info)
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request,'Please verify your email accouant')
            return HttpResponseRedirect(request.path_info)
        user_obj=authenticate(username=username,password=password)
        
        if user_obj:
            login(request,user_obj)
            return render(request,'home.html')
        messages.warning(request,'Invalid Username or Password')
    return render(request,'login.html')


def signup_view(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request,'User already Exists')
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(first_name=first_name,last_name=last_name,
                                       username=username,email=username
                                       )
        cart=Cart.objects.create(user=user_obj,is_paid=False)
        user_obj.set_password(password)
        user_obj.save()
        messages.info(request,'An Email has been sent to your email')
    return render(request,'signup.html')

def activate_email(request,email_token):
    try:
        user=profile.objects.get(email_token=email_token)
        user.is_email_verified=True
        user.save()
        return render(request,'home.html')
    except Exception as e:
        return HttpResponse('Invalid Email Token')