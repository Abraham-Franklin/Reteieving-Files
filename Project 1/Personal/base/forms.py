# from django.forms import ModelForm
from django import forms

class SchoolName(forms.Form):
    school = forms.CharField(max_length=200)
