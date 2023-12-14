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


# class Comments(models.Model):
#     like = models.CharField(max_length=10)
#     love = models.CharField(max_length=10)
#     dislike = models.CharField(max_length=10)
#     heartbreak = models.CharField(max_length=10)
#     laughter = models.CharField(max_length=10)
#     anger = models.CharField(max_length=10)
    
class Posts(models.Model):
    title = models.CharField(max_length=30)
    signupmodel = models.ForeignKey(SignupModel, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # username = models.ForeignKey('SignupModel', related_name='', on_delete=models.CASCADE)
    # comment = models.ForeignKey('Comments', on_delete=models.CASCADE, null=True)
    message_body = models.TextField()
    react = (
        ('like', 'thumbsup'),
        ('dislike', 'thumbsdown'),
        ('love', 'heart'),
        ('hate', 'anger'),
    )
    reaction = models.CharField(max_length=10, choices=react, null=True, blank=True)
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

