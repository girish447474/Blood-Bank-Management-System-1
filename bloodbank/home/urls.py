from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.SignUp, name="signup"),
    path('login/', views.LogIn, name="login"),
    path('logout/', views.user_logout, name="user_logout"),
    path('about/', views.about, name="about"),
    path('profile/', views.profile, name="profile"),
    path('upload/', views.Image_Upload, name="image_upload"),
    path('update_details/', views.Update_Details, name="update_details"),
]
