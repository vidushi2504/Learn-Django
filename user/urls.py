from django.contrib import admin
from django.urls import path
from . import views
from .views import Search_User

urlpatterns = [
	path('', views.userhome, name="userhome"),
	path('post', views.post, name='post'),
	path("comment", views.comment, name="comment"),
	path("user/follow/<str:username>", views.follow, name="follow"),
	path("myprofile", views.myprofile, name="myprofile"),
	path("like_dislike/<int:post_id>", views.likePost, name="like_dislike"),
	path("delete/<intpostId>", views.delPost, name='delPost'),
	path("search/", Search_User.as_view(), name="search_user"),		#use class as a view
	path("<str:username>", views.userProfile, name='userProfile'),
]