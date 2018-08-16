from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def signup_user(request):
	if request.user.is_authenticated:
		return HttpResponse("you are already logged in")
	else:
		if request.method == 'POST':
			form = forms.Register(request.POST)
			if form.is_valid():
				form.save()
				models.Otherdetail(
					user = User.objects.get(username=cleaned_data.get(name='username'))
					).save()
				return HttpResponse('user saved')
			else:
				return render(request,'Userauth/signup.html',{form:'form'})
		else:
			form = forms.Register()
		return render(request,'Userauth/signup.html',{form:'form '})

def login_user(request):
	if request.user.is_authenticated:
		return HttpResponse('you are already logged in')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not none:
				if user.is_active:
					login(request,user)
					return redirect('/User/list/')
				else: 
					return render(request,'Userauth/login.html',{})

			else:
				return render(request,'Userauth/login.html',{})
		else:
			return render(request,'Userauth/login.html',{})



