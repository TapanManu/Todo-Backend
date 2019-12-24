from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import UserForm,UserProfileForm
from .models import UserProfile
from task.models import Task


def register(request):
	registered=False
	profile = UserProfile(user=request.user)

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
		else:
			print("false")
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()
	return render(request,'user/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

	



