from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
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

class PostList(APIView):
    @swagger_auto_schema(
        operation_summary='Lista todos os posts',
        operation_description="Obter informações sobre todos os posts",
        request_body=None,  # opcional
        responses={200: PostSerializer()}
    )
    def get(self, request):
        '''
        Retorna uma lista de posts
        Depende de:
        - APIView
        - Post
        - PostSerializer
        - Response
        :param APIView self: o próprio objeto
        :param Request request: um objeto representando o pedido HTTP 
        :param HTTP: não tem
        :return: uma lista de posts em formato JSON
        :rtype: JSON
        '''
        posts = Post.objects.all().order_by('dt_publicado')
        # importante informar que o queryset terá mais de 1 resultado usando many=True
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Criar post',
        operation_description="Criar um novo post",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'titulo': openapi.Schema(default='Título do Post', description='Título do post', type=openapi.TYPE_STRING),
                'conteudo': openapi.Schema(default='Conteúdo do Post', description='Conteúdo do post', type=openapi.TYPE_STRING),
            },
        ),
        responses={201: PostSerializer(), 400: 'Dados errados'},
    )
    def post(self, request):
        '''
        Cria um novo post
        Depende de:
        - APIView
        - Post
        - PostSerializer
        - Response
        :param APIView self: o próprio objeto
        :param Request request: um objeto representando o pedido HTTP 
        :param HTTP: não tem
        :return: os dados do post criado em formato JSON
        :rtype: JSON
        '''
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
    operation_summary='Atualizar post',
    operation_description="Atualizar um post existente",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'titulo': openapi.Schema(default='Título do Post', description='Título do post', type=openapi.TYPE_STRING),
                'conteudo': openapi.Schema(default='Conteúdo do Post', description='Conteúdo do post', type=openapi.TYPE_STRING),
            },
        ),
        responses={200: PostSerializer(), 400: 'Dados errados'},
        manual_parameters=[
            openapi.Parameter('id_arg', openapi.IN_PATH, default=1, type=openapi.TYPE_INTEGER, required=True, description='ID do post na URL'),
        ],
    )
    def put(self, request, id_arg):
        '''
        Atualiza um post existente
        Depende de:
        - APIView
        - Post
        - PostSerializer
        - Response
        :param APIView self: o próprio objeto
        :param Request request: um objeto representando o pedido HTTP 
        :param int id_arg: o ID do post a ser atualizado
        :return: os dados do post atualizado em formato JSON
        :rtype: JSON
        '''
        try:
            post = Post.objects.get(pk=id_arg)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description='Remove um post',
        request_body=PostSerializer,
        responses={
            204: PostSerializer(), 
            404: None,
        },
    )
    def delete(self, request, id_arg):
        '''
        Remove um post existente
        Depende de:
        - APIView
        - Post
        - PostSerializer
        - Response
        :param APIView self: o próprio objeto
        :param Request request: um objeto representando o pedido HTTP 
        :param int id_arg: o ID do post a ser removido
        :return: uma resposta HTTP sem conteúdo
        :rtype: HTTPResponse
        '''
        try:
            post = Post.objects.get(pk=id_arg)
        except Post.DoesNotExist:
            return Response({'error': f'item [{id_arg}] não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'lista.html')