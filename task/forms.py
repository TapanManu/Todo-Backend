from django import forms
from .models import Task,User

class TaskForms(forms.ModelForm):
	class Meta:
		model=Task
		fields=('task_name',)

class UserForms(forms.ModelForm):
	class Meta:
		model=User
		fields=('username',)		