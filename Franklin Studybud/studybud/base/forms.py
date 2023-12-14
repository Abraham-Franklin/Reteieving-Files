from django import forms
# from .models import
from django.contrib.auth.models import User
from .models import SignupModel

class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password' : forms.PasswordInput(attrs = {'class': 'password'})
        }

class Signup(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password' : forms.PasswordInput(attrs = {'class': 'password'})
        }

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = SignupModel
        fields = '__all__'
        widgets = {
            'password' : forms.PasswordInput(attrs = {'class': 'password'})
        }