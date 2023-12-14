from django.urls import path
from . import views

urlpatterns = [
    path('dict/', views.showout, name='showout'),
    path('test/', views.testing, name='testing'),
    path('djangoforms/', views.home_view, name='djangoforms'),
]