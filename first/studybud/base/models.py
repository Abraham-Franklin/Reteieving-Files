from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class signup(request):

class AddPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=100)
    images_post = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=50, choices=[
        ("Anime", 'Anime'),
        ("Entertainment", 'Entertainment'),
        ("Sports", 'Sports'),
        ("Tech", 'Tech')
    ])
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.topic


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(AddPost, on_delete=models.CASCADE)
    comment_body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_body

class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(AddPost, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user

