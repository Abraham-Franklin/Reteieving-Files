from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserCreation(models.Model):
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username


# class Comments(models.Model):
    # react = (
        #     ('like', 'thumbsup'),
        #     ('dislike', 'thumbsdown'),
        #     ('love', 'heart'),
        #     ('hate', 'anger'),
        # )
        # reaction = models.CharField(max_length=10, choices=react, null=True, blank=True)


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    message_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class Posts(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#     message_body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

