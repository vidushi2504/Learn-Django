from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from user.models import Profile, Following

@receiver(post_save, sender=User)								#sender sends signal
def create_profile(sender, instance, created, **kwargs): 		# created=true, new user created
	if created:													# instance=user object
		Profile.objects.create(user=instance)
		Following.objects.create(user=instance)

@receiver(m2m_changed, sender=Following.followed.through)
def add_follower(sender, instance, action, reverse, pk_set, **kwargs):		#action - pre_add if user followed someone else pre_remove
	followed_users=[]						#list of people current user follows								#pk_set - set of primary keys of following
	logged_user=User.objects.get(username=instance)
	for i in pk_set:
		user=User.objects.get(pk=i)
		following_obj=Following.objects.get(user=user)
		followed_users.append(following_obj)

	if action=="pre_add":			#follow
		for i in followed_users:
			i.follower.add(logged_user)
			i.save()

	if action=="pre_remove":		#unfollow
		for i in followed_users:
			i.follower.remove(logged_user)
			i.save()


