from django.shortcuts import render,get_object_or_404
from .models import Task,User
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForms,UserForms

def home(request):
	user_obj=User.objects.all()
	form=UserForms()
	context={
		'user':user_obj,
		'form':form,
	}
	return render(request,'task/home.html',context)

def createuser(request):
	form=UserForms(request.POST)
	if form.is_valid():
		form.save()
	else:
		print("false")
	return HttpResponseRedirect(reverse('task:home'))	

def login(request):
	if request.method=='POST':
		form=UserForms(request.POST)
		user_obj=User.objects.all()
		if form.is_valid():
			uname=form.cleaned_data['username']
			upass=form.cleaned_data['password']
			for ob in user_obj:
				if (uname == ob.username) and (upass == ob.password):
					return HttpResponse("Logged in successfully")			
	return HttpResponse("Failed to log")


	






def base(request):
	task_obj=Task.objects.all()
	context={
		'task_index':task_obj,
	}
	return render(request,'task/base.html',context)

def index(request):
	task_obj=Task.objects.all()
	form=TaskForms()
	patterns={
		'task_index':task_obj,
		'forms':form,
	}
	return render(request,'task/index.html',patterns)

def create(request):
	form=TaskForms(request.POST)
	if form.is_valid():
		form.save()
	else:
		print("false")	
	return HttpResponseRedirect(reverse('task:index'))

def delete(request,task_id=None):
	task_obj=get_object_or_404(Task,pk=task_id)
	task_obj.delete()
	return HttpResponseRedirect(reverse('task:index'))	
	

