from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name = 'members'),
    path('', views.viewers, name='viewers'),
    path('homePage/', views.tester, name = 'tester'),
]