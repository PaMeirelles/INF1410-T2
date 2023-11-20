from django.urls import path
from .views import PostList, home

app_name = "blog_app"

urlpatterns = [
    path('home/', home, name="home"),
    path('posts/', PostList.as_view(), name='post-list'),
]