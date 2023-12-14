from django.contrib import admin
# from django.contrib.auth.models import User

# Register your models here.
from .models import UserCreation
from .models import Posts
# from .models import Comments

# admin.site.register(User)
admin.site.register(UserCreation)
admin.site.register(Posts)
# admin.site.register(Comments)