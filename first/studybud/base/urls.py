from django.urls import path
from . import views

urlpatterns = [
    path('', views.status, name="status"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('home/', views.home, name="home"),
    path('anime/', views.anime, name="anime"),
    path('readmore/<int:id>/', views.readmore, name="readmore"),
    path('delete-comment/<int:id>/', views.delete_comment, name="delete-comment"),
    path('sports/', views.sports, name="sports"),
    path('tech/', views.tech, name="tech"),
    path('entertainment/', views.entertainment, name="entertainment"),
    path('addpost/', views.addpost, name="addpost"),
    path('user-profile/<int:id>/', views.user_profile, name="user-profile"),
]