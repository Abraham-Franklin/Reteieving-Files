from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content')
