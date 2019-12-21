from django.db import models

# Create your models here.
class Task(models.Model):
	task_name=models.CharField(max_length=200)
	start_time=models.DateTimeField(null=True,blank=True)
	completed=models.BooleanField(blank=True,null=True)
	completed_time=models.DateTimeField(null=True,blank=True)
	def __str__(self):
		return self.task_name

#now i have added some null constraints to all fields for time being,need to develop for the better

class User(models.Model):
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=15,default='password')
	def __str__(self):
		return self.username