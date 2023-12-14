from django.urls import path
from . import views

urlpatterns = [
    path("", views.status, name="status"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("home/", views.home, name="home"),
    path("posts/", views.posts, name="posts"),
    path("viewposts/", views.viewposts, name="viewposts"),
]