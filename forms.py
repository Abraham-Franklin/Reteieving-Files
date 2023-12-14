from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from blog.models import Post, Comment, Like

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = []

    # You can add additional form fields and validation as needed.

