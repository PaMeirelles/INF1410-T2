from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import generics
from django.shortcuts import render
from django.views import View

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'auth/login.html')

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'auth/register.html')

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer