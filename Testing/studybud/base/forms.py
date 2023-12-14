from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import AddPost

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password' : forms.PasswordInput(attrs = {'class': 'password'})
        }

class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())


class PostForm(forms.ModelForm):
    class Meta:
        model = AddPost
        fields = ['topic', 'content', 'image', 'category']