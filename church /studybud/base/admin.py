from django.contrib import admin
from .models import UploadImage, UploadVideo

# Register your models here.
admin.site.register(UploadImage),
admin.site.register(UploadVideo)