from django.urls import path
from . import views

urlpatterns = [
    path('', views.status, name='status'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('home/', views.signin, name='home'),
]