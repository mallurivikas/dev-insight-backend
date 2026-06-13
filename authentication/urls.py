from django.urls import path
from .views import hello, login

urlpatterns = [
    path("hello/", hello),
    path("login/", login),
]