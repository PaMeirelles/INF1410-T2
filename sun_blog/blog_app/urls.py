from django.urls import path
from .views import PostList
from .views import PostListView

app_name = "blog_app"

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
]