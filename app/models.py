from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ArtistInformation(models.Model):
    name = models.CharField(null = True, max_length=255)
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