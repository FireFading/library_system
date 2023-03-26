from django.contrib import admin
from django.urls import path

from .views import logout, signin, signup


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("logout/", logout, name="logout"),
]
