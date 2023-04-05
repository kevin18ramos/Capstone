from django.db import models

# Create your models here.







class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200) 
    date = models.DateField()
    price = price = models.DecimalField(decimal_places=2, max_digits=10)