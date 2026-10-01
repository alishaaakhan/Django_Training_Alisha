from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("signup/", signup, name="signup"),
    path("saveuser/", saveuser, name="saveuser"),
    path("login/", login, name="login"),
    path("loginvalidation/", loginvalidation, name="loginvalidation"),
    path("studentregistration/", studentregistration, name="studentregistration"),
    path("savestudent/", savestudent, name="savestudent"),
    path("success/", success, name="success"),
    path("logout/", logout, name="logout"),
]

