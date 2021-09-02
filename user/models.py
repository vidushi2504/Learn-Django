from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	caption=models.CharField(max_length=500)
	date=models.DateTimeField(auto_now_add=True)
	image=models.ImageField(upload_to="Post", blank=True)

	def __str__(self):
		return str(self.user)+ ' '+ str(self.date.date())

class Profile(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	userImage=models.ImageField(upload_to="Profile", default="default/default.png", blank=True)
	followers=models.IntegerField(default=0)
	following=models.IntegerField(default=0)

	def __str__ (self):
		return str(self.user)

class Like(models.Model):
	user=models.ManyToManyField(User)
	post=models.OneToOneField(Post, on_delete=models.CASCADE)

	@classmethod
	def like(cls, post, likeuser):		#checks if like object for post exists. If it does, increase count by one otherwise, create an object.
		obj, create=cls.objects.get_or_create(post=post)	#if post doesn't exist, null value returned
		obj.user.add(likeuser)
		

	@classmethod
	def dislike(cls, post, dislikeuser):
		obj, create=cls.objects.get_or_create(post=post)
		obj.user.remove(dislikeuser)

	def __str__(self):
		return str(self.post)

class Following(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	followed=models.ManyToManyField(User, related_name="followed")
	follower=models.ManyToManyField(User, related_name="follower")

	@classmethod
	def follow(cls, user, another_account):		#another_account=account to be followed
		obj, create=cls.objects.get_or_create(user=user)
		obj.followed.add(another_account) 

	@classmethod
	def unfollow(cls, user, another_account):
		obj, create=cls.objects.get_or_create(user=user)
		obj.followed.remove(another_account)

	def __str__(self):
		return str(self.user)
