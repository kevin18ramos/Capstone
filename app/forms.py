from django.forms import ModelForm
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from tinymce.widgets import TinyMCE
from django.utils.html import format_html



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']        

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["picture","name",'description',"date","numOfArts","price"]


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")


class MineForm(forms.ModelForm):
    class Meta:
        model = Mine
        fields = ('name','email')