from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'auth/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('/blog/home')
        else:
            return render(request, 'auth/register.html', {'form': form})
        
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('/blog/home')
        
        messages.error(request,f'Invalid username or password')
        return render(request,'auth/login.html',{'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('/blog/home')

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer