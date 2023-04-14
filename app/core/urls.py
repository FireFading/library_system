from core.views import logout, signin, signup
from django.urls import path

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("logout/", logout, name="logout"),
]
