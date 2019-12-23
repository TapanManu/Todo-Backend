from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.DO_NOTHING,)
	website=models.URLField(blank=True)

	def __unicode__(self):
		return self.user.username






