from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ArtistInformation(models.Model):
    name = models.CharField(null = True, max_length=255)
    userAdmin = models.OneToOneField(User,null = True, on_delete=models.CASCADE)
    userName = models.CharField(max_length=200, null=True)
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    websiteLink = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200) 
    date = models.DateField()
    price = price = models.DecimalField(decimal_places=2, max_digits=10)