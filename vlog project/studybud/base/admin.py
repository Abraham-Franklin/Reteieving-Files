from django.contrib import admin

# Register your models here.
from .models import SignupModel
from .models import Posts
# from .models import Comments

admin.site.register(SignupModel)
admin.site.register(Posts)
# admin.site.register(Comments)