from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from .forms import *
import stripe
#from .decorators import *

# home view
def home(request):
    return render(request, 'app/Home.html')

def shoppingcart(request):
    return render(request, 'app/Shopping.html')

def profile(request):
    return render(request, 'app/Profile.html')

# products page
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
    return render(request, 'app/AddProducts.html', {'post_form':form})

def productsPage(request):
    products = Post.objects.all()
    return render(request, 'app/Products.html', {'products':products})


#checkout

class CreateCheckoutSession(APIView):
  def post(self, request):
    dataDict = dict(request.data)
    price = dataDict['price'][0]
    product_name = dataDict['product_name'][0]
    try:
      checkout_session = stripe.checkout.Session.create(
        line_items =[{
        'price_data' :{
          'currency' : 'usd',  
            'product_data': {
              'name': product_name,
            },
          'unit_amount': price
        },
        'quantity' : 1
      }],
        mode= 'payment',
        success_url= FRONTEND_CHECKOUT_SUCCESS_URL,
        cancel_url= FRONTEND_CHECKOUT_FAILED_URL,
        )
      return redirect(checkout_session.url , code=303)
    except Exception as e:
        print(e)
        return e

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
    return render(request,'app/profilepage.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
