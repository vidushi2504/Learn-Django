from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('change_password', views.Change_Password.as_view(), name='change_password'),
]
