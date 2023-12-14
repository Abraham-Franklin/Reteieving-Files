from django.db import models

# Create your models here.
class UploadImage(models.Model):
    image = models.ImageField(upload_to="images/")

class UploadVideo(models.Model):
    video = models.FileField(upload_to="videos/")

