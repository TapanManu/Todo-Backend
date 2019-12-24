from django.shortcuts import render,get_object_or_404
from .models import Task
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForms





def base(request):
	task_obj=Task.objects.all()
	context={
		'task_index':task_obj,
	}
	return render(request,'task/base.html',context)

def index(request,username):
	task_obj=Task.objects.all()
	form=TaskForms()
	patterns={
		'task_index':task_obj,
		'forms':form,
	}
	return render(request,'task/index.html',patterns)

def create(request,username):
	form=TaskForms(request.POST)
	if form.is_valid():
		form.save()
	else:
		print("false")	
	return HttpResponseRedirect(reverse('task:index'),kwargs={'username':username})

def delete(request,task_id,username):
	task_obj=get_object_or_404(Task,pk=task_id)
	task_obj.delete()
	return HttpResponseRedirect(reverse('task:index'))	
	

