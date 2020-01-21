from django.shortcuts import render,get_object_or_404,redirect
from .models import Task
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForms
from user.models import UserProfile
from django.contrib.auth.models import User
from django.utils import timezone

def index(request):
	task_obj=Task.objects.filter(users=request.user)	
	form=TaskForms()
	context={
		'task_index':task_obj,
		'forms':form,
	}
	return render(request,'user/home.html',context)
def create(request,username):
	form=TaskForms(request.POST)
	if form.is_valid():
		#task=Task.objects.create(users=request.user)
		t=form.save(commit=False)
		t.start_time=timezone.now()
		t.users=request.user
		t.save()
	else:
		print("false")	
	return HttpResponseRedirect(reverse('user:home'))

def delete(request,username,task_id):
	task_obj=get_object_or_404(Task,pk=task_id)
	task_obj.delete()
	return HttpResponseRedirect(reverse('user:home'))	

def complete(request,username,task_id):
	form=TaskForms(request.POST)	
	if form.is_valid():
		t=form.save(commit=False)
		t.completed=True
		t.completed_time=timezone.now()
		t.users=request.user
		t.save()
	else:
		print(form.errors)	
	return HttpResponseRedirect(reverse('user:home'))	
