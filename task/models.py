from django.db import models

# Create your models here.
class Task(models.Model):
	task_name=models.CharField(max_length=200)
	start_time=models.DateTimeField('start time')
	completed=models.BooleanField(blank=True)
	completed_time=models.DateTimeField(null=True,blank=True)
	def __str__(self):
		return self.task_name

