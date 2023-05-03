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
     path("products/delete/<int>", views.deleteProducts, name= "deleteProducts"),
     path("products/update/<int>", views.updateProducts, name= "updateProducts"),
     path("products/", views.productsPage, name= "products"),
     path("profilepage/", views.findUser, name= "findUser"),
     path("shoppingcart/", views.shoppingcart, name="shoppingcart"),
     path("settingChange/", views.settingChange, name="settingChange"),
     path('cancel/', CancelView.as_view(), name='cancel'),
     path('success/', SuccessView.as_view(), name='success'),
     path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
     path('landing/', ProductLandingPageView.as_view(), name='landing'),
     path('paypal/', paypal.as_view(), name='paypal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

