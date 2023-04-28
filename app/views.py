from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http.response import HttpResponseNotFound, JsonResponse
from django.urls import reverse, reverse_lazy
import stripe
import json
#from .decorators import *

# home view
def home(request):
    products = Post.objects.all()
    return render(request, 'app/Home.html', {'products':products})

@login_required(login_url = 'login')
def shoppingcart(request):
    return render(request, 'app/Checkout.html')

@login_required(login_url = 'login')
def settingChange(request):
    CurrentUser = request.user
    CurrentArtist = ArtistInformation.objects.get(user=CurrentUser)
    if request.method == 'POST':
        original_password = request.POST.get('original_password')
        password_x1 = request.POST.get('password_x1')
        password_x2 = request.POST.get('password_x2')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        name = request.POST.get('name')
        bio = request.POST.get('bio')

        if original_password != None:
            if CurrentUser.check_password(original_password) == True:
                if password_x1 == password_x2:
                    CurrentUser.set_password(password_x1)
                    CurrentUser.save()     
                    messages.info(request, 'Password is updated.')
                    return redirect('home')
                else:
                    print("password not match")
                    messages.info(request, 'Passwords do not match.')
                    return redirect('home')
            else:
                print("password not match og")
                messages.info(request, 'Passwords is incorrect.')
                return redirect('home')
        elif name != CurrentArtist.name and name != None and name != "":
            try:
                user_with_name = User.objects.get(username=name)
                messages.info(request, 'This username is already taken. Please choose another one.')
                return redirect('settingChange')
            except User.DoesNotExist:
                CurrentUser = request.user
                CurrentUser.username = name
                CurrentUser.save()
                CurrentArtist.name = name
                CurrentArtist.save()
                messages.info(request, 'Username successfully changed.')
                return redirect('settingChange')
        elif firstname != None and firstname != CurrentArtist.firstname and firstname != "":
            CurrentArtist.firstname = firstname
            CurrentArtist.save()
            messages.info(request, 'First name successfully changed.')
            return redirect('settingChange')
        elif lastname != None and lastname != CurrentArtist.lastname and lastname != "":
            CurrentArtist.lastname = lastname
            CurrentArtist.save()
            messages.info(request, 'Last name successfully changed.')
            return redirect('settingChange')
        elif email != None and email != CurrentArtist.email and email != "":
            CurrentArtist.email = email
            CurrentArtist.save()
            messages.info(request, 'Email successfully changed.')
            return redirect('settingChange')
        elif bio != "" and bio != CurrentArtist.bio and bio != None:
            CurrentArtist.bio = bio
            CurrentArtist.save()
            messages.info(request, 'Bio successfully changed.')
            return redirect('settingChange')
        elif request.FILES.get('profilepic'):
            profilepic = request.FILES.get('profilepic')
            CurrentArtist.profile_pic = profilepic
            CurrentArtist.save()
            messages.info(request, 'Profile picture successfully changed.')
            return redirect('settingChange')
     
    return render(request, 'app/settings.html')


@login_required(login_url = 'login')
def profile(request):
    return render(request, 'app/Profile.html')

# add products view
@login_required(login_url = 'login')
def addProductsPage(request):
    form = PostForm(request.POST)
    currentUser = request.user 
    currentUser
    if form.is_valid():
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            form.user = currentUser 
            post = form.save(commit=False) # Save form instance to post variable
            post.user = currentUser # Set user field
            post.save() # Save to the database  
            messages.info(request, 'Product Posted')
            return redirect('home')
    return render(request, 'app/AddProducts.html', {'post_form':form})

# view products view
def productsPage(request):
    products = Post.objects.all()
    return render(request, 'app/Products.html', {'products':products})

#delete products

# #add to cart
# def addToCart(request, itemId):
#     item = Post.objects.get(id=itemId)
#     cartItem, created = Cart.objects.get_or_create(
#         user=request.user,
#         item=item,
#         defaults={
#             'quantity': 1,
#             'price': item.price,
#         }
#     )
#     if not created:
#         cartItem.quantity += 1
#         cartItem.save()
#     return redirect('Cart')


# #checkout
# stripe.api_key = settings.STRIPE_SECRET_KEY

# def checkout(request):
#     cartItems = Cart.objects.filter(user=request.user)
#     total_price = sum([item.price * item.quantity for item in cartItems])
#     if request.method == 'POST':
#         token = request.POST['stripeToken']
#         try:
#             charge = stripe.Charge.create(
#                 amount=int(total_price * 100),
#                 currency='usd',
#                 description='Example charge',
#                 source=token,
#             )
#             for item in cartItems:
#                 item.delete()
#             return redirect('home')
#         except stripe.error.CardError as e:
#             return render(request, 'checkout.html', {'error': e.error.message})
#     return render(request, 'checkout.html', {'total_price': total_price})

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


def findUser(request):
    currentUser = request.user
   
    print(currentUser)
    return render(request,'app/Profile.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
