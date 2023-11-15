from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def hello_world(request):
    """
    A simple API view that returns a "Hello, World!" response.
    """
    return Response({"message": "Hello, World!"})
