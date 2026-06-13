from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializer

@api_view(['GET'])
def hello(request):
    return Response({
        "message": "Hello from Django!"
    })

@api_view(["POST"])
def login(request):

    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        return Response({
            "message": "Login successful!", 
            "data": serializer.validated_data,
        })

    return Response({
        "message": "Login failed!",
        "errors": serializer.errors
    }, status=400)