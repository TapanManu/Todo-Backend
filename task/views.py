from django.shortcuts import render,get_object_or_404
from .models import Task
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForms

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
	

