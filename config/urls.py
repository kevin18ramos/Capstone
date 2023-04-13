from django.contrib import admin
from django.urls import path
from app import views
from app.views import *

urlpatterns = [
     path("admin/", admin.site.urls),
     path("", views.home, name="home"),
     path("login/", views.loginPage, name="login"),
     path("register/", views.registerPage, name="register"),
     path("logout", views.logoutUser, name="logout"),
     path("profile", views.profile, name="profile")
]
