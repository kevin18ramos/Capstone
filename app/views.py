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
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
import stripe
import json
#from .decorators import *

# home view
def home(request):
    return render(request, 'app/Home.html')

@login_required(login_url = 'login')
def shoppingcart(request):
    return render(request, 'app/Checkout.html')

@login_required(login_url = 'login')
def settingChange(request):
    CurrentUser = request.user
    CurrentArtist = ArtistInformation.objects.get(user = CurrentUser)
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
                                print("password not mathc")
                                messages.info(request, 'Passwords do not match.')
                                return redirect('home')
                        else:
                                print("password not mathc og")
                                messages.info(request, 'Passwords is incorrect.')
                                return redirect('home')
                elif name != CurrentUser.username and name != "" :
                    CurrentUser.username = name
                    CurrentUser.save()
                    CurrentArtist.name = name
                    CurrentArtist.save()
                    messages.info(request, 'Username has been changed.')
                    return redirect('settingChange')
                elif firstname != "" and firstname != CurrentArtist.firstname:
                    CurrentArtist.firstname = firstname
                    CurrentArtist.save()
                    messages.info(request, 'Firstname has been changed.')
                    return redirect('settingChange')
                elif lastname != "" and lastname != CurrentArtist.lastname:
                    CurrentArtist.lastname = lastname
                    CurrentArtist.save()
                    messages.info(request, 'Firstname has been changed.')
                    return redirect('settingChange')
                elif email != "" and email != CurrentArtist.email:
                    CurrentArtist.email = email
                    CurrentArtist.save()
                    messages.info(request, 'Firstname has been changed.')
                    return redirect('settingChange')
                elif bio != "" and email != CurrentArtist.bio:
                    CurrentArtist.bio = bio
                    CurrentArtist.save()
                    messages.info(request, 'Firstname has been changed.')
                    return redirect('settingChange')
 
        
    return render(request, 'app/settings.html')


@login_required(login_url = 'login')
def profile(request):
    return render(request, 'app/Profile.html')

<<<<<<< HEAD
# add products view
=======
# products page
@login_required(login_url = 'login')
>>>>>>> newkevin
def addProductsPage(request):
    form = PostForm(request.POST)
    currentUser = request.user
    if form.is_valid():
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            form.user = currentUser 
            post = form.save(commit=False) # Save form instance to post variable
            post.user = currentUser # Set user field
            post.save() # Save to the database
            messages.info(request, 'Product Posted')
            return redirect('products')
    return render(request, 'app/AddProducts.html', {'post_form':form, 'context':settings.STRIPE_PUBLISHABLE_KEY})

# view products view
def productsPage(request):
    products = Post.objects.all()
    return render(request, 'app/Products.html', {'products':products})

#checkout
@csrf_exempt
def create_checkout_session(reqeust, id):
    request_data = json.loads(request.body)
    product = get_object_or_404(Post, pk=id)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        customer_email = request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )

    order = Order()
    order.customer_email = request_data['email']
    order.product = product
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(product.price * 100)
    order.save()

    # return JsonResponse({'data': checkout_session})
    return JsonResponse({'sessionId': checkout_session.id})


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
    currentArtist = ArtistInformation.objects.get(user = currentUser)
    print(currentUser)
    print(currentArtist)
    print(currentArtist.firstname)
    print(currentArtist.lastname)
    print(currentArtist.created_at)
    return render(request,'app/Profile.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
