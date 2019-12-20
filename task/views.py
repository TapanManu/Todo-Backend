from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

def index(request):
	task_obj=Task.objects.all()
	patterns={
		'task_index':task_obj,
	}
	return render(request,'task/index.html',patterns)

def detail(request,task_id):
	return HttpResponse("welcome to details page of %s" %task_id)	
