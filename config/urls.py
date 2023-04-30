from django.contrib import admin
from django.urls import path, include
from app import views
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path("admin/", admin.site.urls),
     path("", views.home, name="home"),
     path("Login/", views.loginPage, name="login"),
     path("Register/", views.registerPage, name="register"),
     path("Profile/", views.profile, name="profile"),
     path("logout/", views.logoutUser, name="logout"),
     path("products/add/", views.addProductsPage, name= "addProducts"),
     path("products/", views.productsPage, name= "products"),
     path("profilepage/", views.findUser, name= "findUser"),
     path('nl', views.letter, name='newsletter'),
     path("shoppingcart/", views.shoppingcart, name="shoppingcart"),
     path("settingChange/", views.settingChange, name="settingChange"),
     path('cart/', views.Cart, name='Cart'),
     path('checkout/', views.checkout, name='checkout'),
     path('newsletter/', views.index, name='index'),
     path('newsletter/', views.index, name='index'),
     path('validate/', views.validate_email, name='validate_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

