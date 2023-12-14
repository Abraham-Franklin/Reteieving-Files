from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class NigeriaStates(models.Model):
    states = models.CharField(max_length=15)
    capitals = models.CharField(max_length=15)