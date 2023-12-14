from django.forms import ModelForm
from django import forms
from .models import UploadImage, UploadVideo

class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = "__all__"
#         widgets = {
#             'image': forms.ImageField(attrs = {"class" : 'input'})
# }
        # widgets = {
        #     'image': forms.ImageField(attrs={'class' : 'image-input', 'accept': 'image/*'})

        #     # 'image' : forms.ImageField(attrs = {"accept" : 'image/*', "class" : 'image-input'})
        # }

class VideoForm(forms.ModelForm):
    class Meta:
        model = UploadVideo
        fields = "__all__"
        # widgets = {
        #     'video': forms.FileField(attrs={'class' : 'video-input', 'accept': 'video/*'}),

        #     # 'video' : forms.FileField(attrs = {"accept" : 'video/*', "class" : 'video-input'})
        # }