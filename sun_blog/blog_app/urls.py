from django.urls import path
from .views import PostList, home
from .views import PostListView
from drf_yasg.utils import swagger_auto_schema

app_name = "blog_app"

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('listaPosts/', PostList.as_view(), name='lista-posts'),
    path('criarPost/', PostList.as_view(), name='criar-post'),
]