<<<<<<< HEAD
=======

# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'password1', 'password2']           

# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ["picture","name",'description',"date","price"]

>>>>>>> 3acea72a27b8563b2e4b64fd58437e47afbc32d8
from django.forms import ModelForm
from .models import Post
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']           

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["picture","name",'description',"date","price"]
<<<<<<< HEAD
=======

>>>>>>> 3acea72a27b8563b2e4b64fd58437e47afbc32d8
