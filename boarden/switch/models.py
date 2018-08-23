from django.db import models


# Create your models here.


class Vocabulary(models.Model):
	vocab 		=	models.CharField(max_length = 50)
	inputdate 	=	models.DateField(auto_now=False)
	
