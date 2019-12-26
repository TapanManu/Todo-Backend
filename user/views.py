from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import UserForm,UserProfileForm
from .models import UserProfile
from task.models import Task
from django.contrib import auth 


def register(request):
	registered=False

	if request.method=='POST':
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()
			registered=True
			auth.login(request,user)
			context={
			'user':user,
			}
			return render(request,'user/home.html',context)

		else:
			print("false")
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()
	return render(request,'user/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



def logi(request):
	user_form=UserForm(data=request.POST)
	profile_form=UserProfileForm(data=request.POST)
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username,password=password)
		if user.is_authenticated:
			auth.login(request,user)
			context={
			'user':user,
			}
			return render(request,'user/home.html',context)	
		else:
			return HttpResponseRedirect(reverse('user:home'))	
	return render(request,'user/logi.html',{'user_form':user_form,'profile_form':profile_form})

def logo(request):
	auth.logout(request)
	return render(request,'user/logo.html')


	



