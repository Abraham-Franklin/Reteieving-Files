from django.urls import path
from . import views

urlpatterns = [
    path('', views.status, name="status"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signup-admin/', views.signup_admin, name="signup-admin"),
    path('signin-admin/', views.signin_admin, name="signin-admin"),
    path('home/', views.home, name="home"),
    path('add-post/', views.addpost, name="add-post"),
]
