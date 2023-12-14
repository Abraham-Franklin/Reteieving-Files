from django import forms
# from .forms import ModelForm
from .models import SignupModel

class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupModel
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs = {"class" : 'input'}),
            'firstname': forms.TextInput(attrs = {"class" : 'input'}),
            'lastname': forms.TextInput(attrs = {"class" : 'input'}),
            'email': forms.TextInput(attrs = {"class" : 'input'}),
            'password': forms.PasswordInput(attrs = {"class" : 'input'}),
            'c_password': forms.PasswordInput(attrs = {"class" : 'input'})
        }

class SigninForm(forms.ModelForm):
    class Meta:
        model = SignupModel
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs = {"class" : 'input'}),
            'password': forms.PasswordInput(attrs = {"class" : 'input'})
        }