from django.db import models
from django.contrib.auth.models import User
from task.models import Task

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.DO_NOTHING,)
	tasks=models.ForeignKey(Task,on_delete=models.CASCADE)
	website=models.URLField(blank=True)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username	
