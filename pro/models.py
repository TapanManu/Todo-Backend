from django.db import models

# Create your models here.
class Profile(models.Model):
	first_name=models.CharField(max_length=30,default="")
	last_name=models.CharField(max_length=30,default="")
	age=models.IntegerField()

class Post(models.Model):
	SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
	details=models.ForeignKey(Profile,on_delete=models.CASCADE,default=False)
	comment=models.TextField(blank=True)
	sizes=models.CharField(max_length=1,choices=SHIRT_SIZES)


