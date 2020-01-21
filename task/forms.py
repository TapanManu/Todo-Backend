from django import forms
from .models import Task

class TaskForms(forms.ModelForm):
	class Meta:
		model=Task
		fields=('task_name','start_time',)
		exclude=('completed','completed_time',)


	#def save(self,*args,**kwargs):
 	#	user=super().save(commit=False)
 	#	user.save()
	#	task=Task.objects.create(users=user)
	#	return user