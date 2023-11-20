from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.sign_up, name='register'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
