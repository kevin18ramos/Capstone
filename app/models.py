
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from urllib import request
# Create your models here.

class ArtistInformation(models.Model):
    profile_pic = models.ImageField(default="images/cabbage.jpg", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(null = True, max_length=255)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    websiteLink = models.URLField(max_length=200, null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', null = True, blank = True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200) 
    date = models.DateField()
    numOfArts = models.IntegerField(default=1)
    price = price = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Post, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    customer_email = models.EmailField(default='default@gmail.com')
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(default=False)



class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    # Date_Created = models.DateTimeField(False, True, editable=False)


    def __str__(self):
        return self.email



class Mine(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()




