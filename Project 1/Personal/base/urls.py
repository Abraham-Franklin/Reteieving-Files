from django.urls import path
from . import views

urlpatterns = [
    path('', views.printout, name='printout'),
    path('', views.showcase, name='showcase'),
    path('showcase/', views.showcase, name='showcase'),
]