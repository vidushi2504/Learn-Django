from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

def home(request):
	return render(request, 'media/signup.html')

def signup(request):
	if request.method=='POST':
		mail=request.POST.get('email', '')
		username=request.POST.get('username', '')
		name=request.POST.get('name', '')
		password=request.POST.get('password', '')
		confirmpassword=request.POST.get('confirmpassword', '')
		userCheck=User.objects.filter(username=username) | User.objects.filter(email=mail)
		if userCheck:
			messages.error(request, "Username or email already exits!")
			return redirect('/')
		if password==confirmpassword:
			user_obj=User.objects.create_user(first_name=name, password=password, email=mail, username=username)
			user_obj.save()
		return redirect('/')

def userlogin(request):
	if request.method=="POST":
		user_name=request.POST.get('username', '')
		user_password=request.POST.get('password', '')

		# to check if such a user exists

		user=authenticate(username=user_name, password=user_password)

		#authenticate will return name if exists, otherwise none
		if user is not None:
			login(request, user)
			messages.success(request, "Logged In")
			return redirect('/user')
		else:
			messages.error(request, "Invalid Credentials")
			return redirect('/')

def userlogout(request):
	logout(request)
	messages.success(request, "Succesfully Logged Out")
	return redirect("/")

class Change_Password(TemplateView):	#class based view
	template_name="media/password_change.html"

	def post(self, request):
		form=PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, user=request.user)
			messages.success(request, "Password changed successfully!")
			return redirect("/")
		else:
			for err in form.errors.values():
				messages.error(request, err)
			return redirect("/change_password")

	def get(self, request):
		form=PasswordChangeForm(user=request.user)
		return render(request, self.template_name, {"form":form})