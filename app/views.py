from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .decorators import *

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def loginPage(request):
    if request.ArtistInformation.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            artist = authenticate(request, name=username, password=password)
            if artist is not None:
                login(request, artist)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password Is Incorrect')
                return redirect('login')
        return render(request,'app/login.html')

def registerPage(request):
    if request.ArtistInformation.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                artist = form.save()
                username = form.cleaned_data.get('username')
                firstname = form.cleaned_data.ge0t('firstname')
                lastname = form.cleaned_data.get('lastname')
                email = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + username)
                ArtistInformation.objects.create(
                    name=username,
                    firstName=firstname,
                    lastName=lastname,
                    email=email
                )
                return redirect('login')
        context = {'form':form}
        return render(request,'app/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
