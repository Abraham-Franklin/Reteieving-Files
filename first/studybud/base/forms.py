from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import AddPost
# from django.contrib.auth.models import User

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs = {"class" : 'input'}),
            'firstname': forms.TextInput(attrs = {"class" : 'input'}),
            'lastname': forms.TextInput(attrs = {"class" : 'input'}),
            'password': forms.PasswordInput(attrs = {"class" : 'input'})
}

# class SigninForm(forms.Form):
#     username = forms.TextInput(attrs = {'class' : "username"})
#     password = forms.PasswordInput(attrs = {'class' : "password"})


class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs = {"class" : 'input'}),
            'password': forms.PasswordInput(attrs = {"class" : 'input'})
}



class AddPostForm(forms.ModelForm):
    class Meta:
        model = AddPost
        fields = "__all__"
        # fields = ['topic', 'category', 'images_post', 'body']
        exclude = ['user']