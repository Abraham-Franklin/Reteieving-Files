from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignupModel(models.Model):
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username