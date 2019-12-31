from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.DO_NOTHING,)
	website=models.URLField(blank=True)

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.user.username	




		#may be add models.ManytoManyField here to get full working performance
