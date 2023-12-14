from django.db import models
# from .models import Model
from django.contrib.auth.models import User

# Create your models here.
class SignupModel(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
