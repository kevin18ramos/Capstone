from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse,  HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http.response import HttpResponseNotFound, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from paypal.standard.forms import PayPalPaymentsForm
import uuid

from django.core.validators import ValidationError
import re
from .models import SubscribedUsers
from django.core.mail import send_mail
from django.core.mail import EmailMessage
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
    CurrentUrl = Url.objects.get(user=CurrentUser)
    CurrentArtist = ArtistInformation.objects.get(user=CurrentUser)
    form = PostForm(request.POST)
    currentUser = request.user 
    try:
        deleteId = Post.objects.get(user=currentUser)
    except:
        print('User has not made a post yet.')
        deleteId = ""
         
    if request.method == 'POST':
        original_password = request.POST.get('original_password')
        password_x1 = request.POST.get('password_x1')
        password_x2 = request.POST.get('password_x2')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        PersonalLink = request.POST.get('PersonalLink')
        Instalink = request.POST.get('Instalink')
        Facebooklink = request.POST.get('Facebooklink')
        Twitterlink = request.POST.get('Twitterlink')
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
        elif lastname != None and lastname != CurrentArtist.lastname and lastname != "":
                print("went through the elif")
                CurrentArtist.lastname = lastname
                CurrentArtist.save()
                print("went through the save")
                messages.info(request, 'First name successfully changed.')
                return redirect('settingChange')
        elif PersonalLink != None and PersonalLink != CurrentUrl.PersonalLink and PersonalLink != "":
            CurrentUrl.PersonalLink = PersonalLink
            CurrentUrl.save()
            messages.info(request, 'Last name successfully changed.')
            return redirect('settingChange')
        elif Instalink != None and Instalink != CurrentUrl.Instalink and Instalink != "":
            CurrentUrl.Instalink = Instalink
            CurrentUrl.save()
            messages.info(request, 'Last name successfully changed.')
            return redirect('settingChange')
        elif Facebooklink != None and Facebooklink != CurrentUrl.Facebooklink and Facebooklink != "":
            CurrentUrl.Facebooklink = Facebooklink
            CurrentUrl.save()
            messages.info(request, 'Last name successfully changed.')
            return redirect('settingChange')
        elif Twitterlink != None and Twitterlink != CurrentUrl.Twitterlink and Twitterlink != "":
            CurrentUrl.Twitterlink = Twitterlink
            CurrentUrl.save()
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
        else:
            currentUser = request.user  
            #checks whether the current artist has any post
            posted = Post.objects.filter(user=currentUser).first() # use .first() to retrieve a single instance
            form = PostForm(request.POST, request.FILES, instance=posted) # pass the instance to the form
            if form.is_valid():
                if Post.objects.filter(user=currentUser).exists():
                    if request.method == "POST":
                        form = PostForm(request.POST, request.FILES, instance=posted)
                        if form.is_valid():
                            form.save()
                            messages.info(request, 'Product successfully changed.')
                            return redirect ('settingChange')
                    else:
                        form = PostForm(instance=posted)  
                # updates instead of adding to preexisting object
                else:                                                             
                    form = PostForm(request.POST, request.FILES)
                    post = form.save(commit=False) # Save form instance to post variable
                    post.user = currentUser # Set user field
                    post.save() # Save to the database  
                    messages.info(request, 'Product Posted')
                    return redirect('settingChange')
                
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        print(f"{field}: {error}")    
            return render(request, 'app/settings.html', {'post_form' : form, 'deleteId':deleteId})
    return render(request, 'app/settings.html', {'post_form' : form, 'deleteId':deleteId})


@login_required(login_url = 'login')
def profile(request):
    return render(request, 'app/Profile.html')

@login_required(login_url = 'login')
def personalProfile(request,pk):
    Artist = ArtistInformation.objects.get(id = pk)
    useronscreen = Artist.user
    userpost = Post.objects.get(user = useronscreen)
    Urlperson = Url.objects.get(id = pk)
    context = {'Urlperson':Urlperson,'Artist':Artist, 'userpost':userpost}
    return render(request, 'app/ProfileforClick.html',context)

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
        messages.info(request, 'Product successfully changed.')
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

def payMe(request, postId):
    postDetails = Post.objects.get(id=postId)
    artistDetails = ArtistInformation.objects.get(user = postDetails.user)
    paypal_dict = {
        'business': artistDetails.email,
        'amount': postDetails.price,
        'item_name': postDetails.name,
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': request.build_absolute_uri(reverse("paypal-ipn")),
        'return': request.build_absolute_uri(reverse("paypal-reverse")),
        'cancel_return': request.build_absolute_uri(reverse("paypal-cancel")),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'form':form}
    return render(request,'app/paypalpayment.html',context)
                  
def paypal_reverse(request, postId):
    messages.success(request, "you've made the payment")
    postDetails = Post.objects.filter(id=postId)
    postDetails.delete()
    return redirect('home')

def paypal_cancel(request, postId):
    messages.success(request, "payment canceled")
    return redirect('home')

class paypal(TemplateView):
    template_name = "app/paypal.html"       

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
                Url.objects.create(
				user = user,
                PersonalLink = "",
                Instalink = "https://www.instagram.com",
                Facebooklink = "https://www.facebook.com",
                Twitterlink = "https://twitter.com"
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







def index(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)
        subscribedUsers = SubscribedUsers()
        subscribedUsers.email = email
        subscribedUsers.name = name
        # subscribedUsers.full_clean ()
        subscribedUsers.save()
        # send a confirmation mail
        subject = 'NewsLetter Subscription'
        message = 'Hello ' + name + ', Thanks for subseibing us. You will get notification of latest  posted art on our website. Please do not reply on this email.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list,  fail_silently=True)
        res = JsonResponse({'msg': 'Thanks. Subscribed Successfully!'})
        return res
    return render(request, 'app/index.html')

def validate_email(request): 
    email = request.POST.get("email", None)   
    if email is None:
        res = JsonResponse({'msg': 'Emaiil is required.'})
    elif SubscribedUsers.objects.get(email = email):
        res = JsonResponse({'msg': 'Email Address already exists'})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg': 'Invalid Email Address'})
    else:
        res = JsonResponse({'msg': ''})
    return res


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, settings.EMAIL_HOST_USER, bcc=receivers)
            mail.content_subtype = 'html'
            mail.send()

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect("/")

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join([active.email for active in SubscribedUsers.objects.all()])
    return render(request=request, template_name='app/newsletter.html', context={'form': form})


# def letter(request):
#     return render(request, 'app/newsletter.html')

