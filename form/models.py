from django.db import models

class Contactform(models.Model):
	name = models.CharField(max_length=30)
	body = models.TextField()
	date = models.DateTimeField()
	email = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	

# Create your models here.
