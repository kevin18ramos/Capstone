from django.contrib import admin
from django.urls import path
from app import views
from app.views import *

urlpatterns = [
     path("admin/", admin.site.urls),
     path("", views.home, name="home"),
     path("Login", views.LoginPage, name="Login"),
     path("Register", views.RegisterPage, name="Register"),
]
