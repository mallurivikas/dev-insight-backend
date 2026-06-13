from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET'])
def hello(request):
    return Response({
        "message": "Hello from Django!"
    })

@api_view(["POST"])
def login(request):

    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({
        "message": "Login failed!",
        "errors": serializer.errors
        }, status=400)

    data = serializer.validated_data

    user = authenticate(
    username=data["username"],
    password=data["password"]
    )

    if user is None:
        return Response({
        "message": "Invalid credentials!"
        }, status=401)
    
    refresh = RefreshToken.for_user(user)

    return Response({
        "success": True,
        "message": "Login successful",
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
    })


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({
        "message": "Welcome!",
        "user": request.user.username
    })