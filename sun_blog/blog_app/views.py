from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render

# @authentication_classes([])
# @permission_classes([IsAuthenticated])
def home(request):
    return render(request, "blog/home.html")

from django.views import View
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema




class PostList(APIView):
    @swagger_auto_schema(
        operation_summary='Lista todos os posts',
        operation_description="Obter informações sobre todos os carros",
        request_body=None,  # opcional
        responses={200: PostSerializer()}
    )
    def get(self, request):
        posts = Post.objects.all().order_by('dt_publicado')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class PostListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'lista.html')