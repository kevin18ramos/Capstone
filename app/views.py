from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def LoginPage(request):
    return render(request, 'Login.html')

def RegisterPage(request):
    return render(request, 'Register.html')