from django.db import models

# Create your models here.

class Engineer(models.Model):
	name 			= models.CharField(max_length = 100)
	emailID			= models.CharField(max_length = 100)
	engineer_group 	= models.CharField(max_length = 100)