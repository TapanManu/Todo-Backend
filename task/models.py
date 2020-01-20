from django.db import models
from user.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	task_name=models.CharField(max_length=200)
	start_time=models.DateTimeField(null=True,blank=True)
	completed=models.BooleanField(blank=True,null=True)
	completed_time=models.DateTimeField(null=True,blank=True)
	users=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
	profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True,blank=True)
	def __str__(self):
		return self.task_name

#now i have added some null constraints to all fields for time being,need to develop for the better


