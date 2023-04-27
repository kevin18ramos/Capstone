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
        fields = ["picture","name",'description',"date","numOfArts","price"]

class PhotoForm(ModelForm):
    class Meta:
        model = ArtistInformation
        fields = ["profile_pic"]
        
