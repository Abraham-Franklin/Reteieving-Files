from django.urls import path
from . import views

urlpatterns = [
    path('', views.showout, name='showout')
]