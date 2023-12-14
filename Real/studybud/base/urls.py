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
    path('view-post/', views.view_post, name="view-post"),
    path('category/', views.category, name="category"),
    path('edit-post/<str:pk>/', views.edit_post, name="edit-post"),
    path('delete-post/<str:pk>/', views.delete_post, name="delete-post"),
    path('delete-comment/<str:pk>/', views.delete_comment, name="delete-comment"),
    path('readmore/<str:pk>/', views.read_more, name="readmore"),
]
