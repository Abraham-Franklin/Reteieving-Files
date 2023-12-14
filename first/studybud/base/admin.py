from django.contrib import admin
from .models import AddPost, Comments, Reaction

# Register your models here.
admin.site.register(AddPost)
admin.site.register(Comments)
admin.site.register(Reaction)