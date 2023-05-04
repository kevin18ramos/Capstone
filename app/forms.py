from django.forms import ModelForm
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.utils.html import format_html

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']        

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["picture","name",'description',"date","numOfArts","price"]
