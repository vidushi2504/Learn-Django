from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Post, Profile, Like, Following
from django.contrib.auth.models import User
import json
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.
def userhome(request):
	#fetch data from database
	user=Following.objects.get(user=request.user)
	followed_users=[i for i in user.followed.all()]
	followed_users.append(request.user)
	posts=Post.objects.filter(user__in=followed_users).order_by("-pk")
	liked_posts=[i for i in posts if Like.objects.filter(post = i, user = request.user)]
	data={'posts':posts,
		   'liked_post':liked_posts
		 }
	return render(request, "user/postfeed.html", data)

def post(request):
	if request.method=="POST":
		if bool(request.FILES.get('image', False)) == True:
			image_=request.FILES.get('image')
		else:
			image_='';
		caption_=request.POST.get('caption', '')
		user_=request.user
		post_obj=Post(user=user_, caption=caption_, image=image_)
		post_obj.save()
		messages.success(request, "Posted successfully!")
		return redirect('/user')
	else:
		messages.error(request, "Something went wrong!")
		return redirect('/user')

def delPost(request, ID):
	post_=Post.objects.filter(pk=ID)
	#image_path=post_[0].image.url		#image location
	post_.delete()
	messages.info(request, "Post deleted successfully")
	return redirect('/user')

def userProfile(request, username):
	user=User.objects.filter(username=username)		#if not present, filter gives empty list. get gives error
	if user:
		user=user[0]
		profile=Profile.objects.get(user=user) 		#get returns object. filter returns list
		user_img=profile.userImage
		post=user_profile_posts(user)
		is_following=Following.objects.filter(user=request.user, followed=user)
		followingObj=Following.objects.get(user=user)
		followers, following=followingObj.follower.count(), followingObj.followed.count()
		data={'user_obj':user, 
				'followers':followers, 
				'following':following,
				'userImg':user_img,
				'posts':post,
				'connection':is_following 
			 }
	else:
		return HttpResponse("No such user")
	return render(request, 'user/userProfile.html', data)

def likePost(request, post_id):
	#post_id=request.GET.get("likeID", "")
	post=Post.objects.get(pk=post_id)
	user=request.user
	like=Like.objects.filter(post=post, user=user)
	liked=False

	if like:		#if user already in list
		Like.dislike(post, user)
	else:			#if not in list
		liked=True
		Like.like(post, user)

	resp={
		"liked":liked,
	}
	response=json.dumps(resp)
	return HttpResponse(response, content_type="application/json")


def comment(request):
	return render(request, 'user/comments.html')

def user_profile_posts(user):
	posts=Post.objects.filter(user=user)
	return posts

def myprofile(request):
	return HttpResponse("My profile")

def follow(request, username):
	main_user=request.user
	to_follow=User.objects.get(username=username)

	#check if already following
	following=Following.objects.filter(user=main_user, followed=to_follow)
	is_following=True if following else False

	if is_following:
		Following.unfollow(main_user, to_follow)
		is_following=False
	else:
		Following.follow(main_user, to_follow)
		is_following=True

	resp={
		"following":is_following,		#returning response whether followed or not
	}
	response=json.dumps(resp)
	return HttpResponse(response, content_type="application/json")

class Search_User(ListView):		#class based view #inherit ListView
	model=User	
	template_name="user/searchUser.html"
	paginate_by=5
	def get_queryset(self):
		username=self.request.GET.get("username", "")
		queryset=User.objects.filter(username__icontains=username)		#partially matching username also included. i=case insensitive
		return queryset