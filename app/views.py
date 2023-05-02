from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.views import View
from .models import stripePrice
from django.views.generic import TemplateView
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
    form = PostForm(request.POST)
    currentUser = request.user 
    print("went through the user")
    
   
         
    if request.method == 'POST':
        original_password = request.POST.get('original_password')
        password_x1 = request.POST.get('password_x1')
        password_x2 = request.POST.get('password_x2')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        name1 = request.POST.get('name1')
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
        elif name1 != CurrentArtist.name and name1 != None and name1 != "":
                try:
                    user_with_name = User.objects.get(username=name1)
                    messages.info(request, 'This username is already taken. Please choose another one.')
                    return redirect('settingChange')
                except User.DoesNotExist:
                    CurrentUser = request.user
                    CurrentUser.username = name1
                    CurrentUser.save()
                    CurrentArtist.name = name1
                    CurrentArtist.save()
                    messages.info(request, 'Username successfully changed.')
                    return redirect('settingChange')
        elif firstname != None and firstname != CurrentArtist.firstname and firstname != "":
                print("went through the elif")
                CurrentArtist.firstname = firstname
                CurrentArtist.save()
                print("went through the save")
                messages.info(request, 'First name successfully changed.')
                return redirect('settingChange')
            # elif Instalink != None and Instalink != CurrentArtist.Instalink and Instalink != "":
            #     CurrentArtist.Instalink = Instalink
            #     CurrentArtist.save()
            #     messages.info(request, 'Last name successfully changed.')
            #     return redirect('settingChange')
            # elif Facebooklink != None and Facebooklink != CurrentArtist.Facebooklink and Facebooklink != "":
            #     CurrentArtist.Facebooklink = Facebooklink
            #     CurrentArtist.save()
            #     messages.info(request, 'Last name successfully changed.')
            #     return redirect('settingChange')
            # elif Twitterlink != None and Twitterlink != CurrentArtist.Twitterlink and Twitterlink != "":
            #     CurrentArtist.Twitterlink = Twitterlink
            #     CurrentArtist.save()
            #     messages.info(request, 'Last name successfully changed.')
            #     return redirect('settingChange')
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
        else:
            currentUser = request.user  
            #checks whether the current artist has any post
            posted = Post.objects.filter(user=currentUser).first() # use .first() to retrieve a single instance
            form = PostForm(request.POST, request.FILES, instance=posted) # pass the instance to the form
            if form.is_valid():
                if posted is None:
                    form = PostForm(request.POST, request.FILES)
                    post = form.save(commit=False) # Save form instance to post variable
                    post.user = currentUser # Set user field
                    post.save() # Save to the database  
                    messages.info(request, 'Product Posted')
                    return redirect('settingChange')
                
                # updates instead of adding to preexisting object
                else:                                                             
                    if request.method == "POST":
                        form = PostForm(request.POST, request.FILES, instance=posted)
                        if form.is_valid():
                            form.save()
                            messages.info(request, 'Product successfully changed.')
                            return redirect ('settingChange')
                    else:
                        form = PostForm(instance=posted)  
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        print(f"{field}: {error}")    
            return render(request, 'app/settings.html', {'post_form' : form})
    return render(request, 'app/settings.html', {'post_form' : form})


@login_required(login_url = 'login')
def profile(request):
    return render(request, 'app/Profile.html')

@login_required(login_url = 'login')
# view products view
def productsPage(request):
    products = Post.objects.all()
    return render(request, 'app/Products.html', {'products':products})

#delete products view
def deleteProducts(request, id):
    context = {}
    delete_object = Post.objects.get(id=id)
    current_user = request.user
    if current_user == delete_object.user:
        Post.objects.get(id=id).delete()
        return HttpResponseRedirect("/home/")
    return render(request, '', context)

#update products view
def updateProducts(request, id):                                       
    data = get_object_or_404(Post, id=id)
    form = PostForm(instance=data)                                                               
    if request.method == "POST":
        form = PostForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {
        "form":form
    }
    return render(request, '', context)

stripe.api_key = settings.STRIPE_SECRET_KEY
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = stripePrice.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)

class ProductLandingPageView(TemplateView):
    template_name = "app/landing.html"
    def get_context_data(self, **kwargs):
        post = Post.objects.get(name="guts")
        prices = stripePrice.objects.filter(post=post)
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": post,
            "prices": prices
        })
        return context
        
class SuccessView(TemplateView):
    template_name = "app/success.html"

class CancelView(TemplateView):
    template_name = "app/cancel.html"

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
    if request.user.is_authenticated:
        return redirect('home')
    else:
        user_form = CreateUserForm()
        print("before post")
        if request.method == 'POST':
            print("after post")
            user_form = CreateUserForm(request.POST)
            print(user_form.errors)
            if user_form.is_valid():
                print("after valid")
           
                user = user_form.save(commit=False)
                user.save()
                print("user artist")
                ArtistInformation.objects.create(
				user = user,
                name = user.username
			)
              
                print("after artist")
                messages.success(request, 'Account was created for ' + user.username)
                return redirect("settingChange")

        context = {'user_form': user_form}
    return render(request,'app/Register.html', context)


def findUser(request):
    currentUser = request.user
   
    print(currentUser)
    return render(request,'app/Profile.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
