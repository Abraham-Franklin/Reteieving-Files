from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignupModel(models.Model):
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username

    
    