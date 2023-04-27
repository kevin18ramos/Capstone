
from django.db import models



from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
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
    cart = models.CharField(max_length=200,null=True)

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
    
class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(to=Post, on_delete=models.PROTECT)
    amount = models.IntegerField()
    customer_email = models.EmailField()
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(default=False)
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # art = models.ForeignKey(User, on_delete=models.CASCADE)
    # totalprice = models.IntegerField()
    

    def add_to_cart(self):
        pass
        # if request.user.is_authenticated:
        #     cart = Cart.objects.filter(user=request.user)
        # cart.items.add(id)


    def get_total_price(self):
        pass




