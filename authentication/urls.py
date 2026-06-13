from django.urls import path
from .views import hello, login, profile

urlpatterns = [
    path("hello/", hello),
    path("login/", login),
    path("profile/",profile),
]