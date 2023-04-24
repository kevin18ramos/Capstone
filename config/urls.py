from django.contrib import admin
from django.urls import path
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
<<<<<<< HEAD
     path("shoppingcart/", views.shoppingcart, name="shoppingcart"),
     path("Login/Register/", views.register, name="register"),
=======
     path("shoppingcart", views.shoppingcart, name="shoppingcart"),
     path("Login/Register/", views.registerPage, name="register")
>>>>>>> 0eaaebc27e9fc73f42ca2a21624d7fd3589ac37e
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

