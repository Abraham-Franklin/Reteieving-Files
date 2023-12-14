from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SignupModel(models.Model):
    username = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.username

# class SigninModel(models.Model):
#     username = models.CharField(max_length = 200)
#     password = models.CharField(max_length = 200)

    # def __str__(self):
    #     return self.username



# declare a new model with a name "GeeksModel"
# class GeeksModel(models.Model):
#     # fields of the model
#     title = models.CharField(max_length = 200)
#     description = models.TextField()
#     last_modified = models.DateTimeField(auto_now_add = True)
#     img = models.ImageField(upload_to = "images/")

#     # renames the instances of the model
#     # with their title name
#     def __str__(self):
#         return self.title