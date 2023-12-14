from django import forms
from .models import SignupModel

# Creatin a form
class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupModel
        fields = '__all__'

class SigninForm(forms.Form):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)