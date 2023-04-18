from django.contrib import admin
from django.urls import path
from app import views
from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path("admin/", admin.site.urls),
     path("", views.home, name="home"),
     path("login/", views.loginPage, name="login"),
     path("register/", views.registerPage, name="register"),
     path("profile", views.profile, name="profile"),
     path("logout/", views.logoutUser, name="logout"),
     path("products/add/", views.addProductsPage, name= "addProducts"),
     path("products/", views.productsPage, name= "products"),
     path("profilepage/", views.findUser, name= "findUser"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
