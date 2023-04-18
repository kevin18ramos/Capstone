from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'app/Home.html')

def login(request):
    return render(request, 'app/Login.html')

def register(request):
    return render(request, 'app/Register.html')

def profile(request):
    return render(request, 'app/Profile.html')