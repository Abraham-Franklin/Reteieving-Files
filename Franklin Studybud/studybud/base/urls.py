from . import views
from django.urls import path

urlpatterns = [
    path('', views.status, name = 'status'),
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('home/', views.home, name = 'home'),
]