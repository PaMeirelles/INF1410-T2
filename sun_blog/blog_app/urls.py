from django.urls import path
from .views import PostList

app_name = "blog_app"

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
]