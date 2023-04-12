from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from .forms import *
#from .decorators import *

# home view
def home(request):
    return render(request, 'app/Home.html')

def addProductsPage(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                messages.info(request, 'Product Posted')
        return render(request, 'AddProducts.html', {'form':form})
    else:
        return redirect('login')




#login register and logout
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
                    username = request.POST.get('username')
                    password = request.POST.get('password')
                    user = authenticate(request, username=username,password=password)

                    if user is not None:
                        login(request, user)
                        return redirect('home')
                    else:
                        messages.info(request, 'Username or Password Is Incorrect')
                        return redirect('login')

        return render(request,'app/Login.html')


        

def registerPage(request):
    print("register")
    if request.user.is_authenticated:
        print("authenticated")
        return redirect('home')
    else:
        print("unauthenticated")
        form = CreateUserForm()
        if request.method == 'POST':
            print("post")
            form = CreateUserForm(request.POST)
            if form.is_valid():
                print("form")
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
                ArtistInformation.objects.create(
				user = user,
                name = user.username
			)
                
            return redirect("login")
        context = {'form':form}
        return render(request,'app/Register.html',context)



def logoutUser(request):
    logout(request)
    return redirect('login')
