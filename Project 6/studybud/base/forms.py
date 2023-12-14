from django import forms
from .models import SignupModel
# from django import forms

# Creating a form
class SignupField(forms.ModelForm):
    class Meta:
        model = SignupModel
        fields = '__all__'
    
class SigninField(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(max_length = 200)


# class GeeksForm(forms.ModelForm):
#     # specify the name of model to use
#     class Meta:
#         model = GeeksModel
#         fields = "__all__"