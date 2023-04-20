
from django.db import models



from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class ArtistInformation(models.Model):
    profile_pic = models.ImageField(default="Bojack.png", null=True, blank=True)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pics/', null = True, blank = True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200) 
    date = models.DateField()
    price = price = models.DecimalField(decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.name
