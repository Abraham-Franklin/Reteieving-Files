from django import forms
from django.contrib.auth.models import User
from .models import User, Posts

# Creatin a form
# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = UserCreation
#         fields = '__all__'

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-tag'}),
            # 'firstname': forms.TextInput(attrs={'class': 'input-tag'}),
            # 'lastname': forms.TextInput(attrs={'class': 'input-tag'}),
            'email': forms.EmailInput(attrs={'class': 'input-tag'}),
            'password': forms.PasswordInput(attrs={'class': 'input-tag'}),
        }

class SigninForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'