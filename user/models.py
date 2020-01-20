from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	website=models.URLField(blank=True)

	def __unicode__(self):
		return self.website

	def __str__(self):
		return self.website

	


		#may be add models.ManytoManyField here to get full working performance
