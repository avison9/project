from django.db import models
from django.contrib.auth.models import User 
# from model_utils import Choices


class Subjects(models.Model):
	subject = models.CharField(max_length=100)

	def __str__(self):
		return self.subject

class Student(models.Model):
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length= 100)
	last_name = models.CharField(max_length= 100)
	gender = models.CharField(max_length= 2)
	D_O_B = models.DateTimeField()
	address = models.CharField(max_length=300)
	parent_contact = models.IntegerField()
	student_class = models.IntegerField()
	student_club = models.CharField(max_length=100)
	# student_catergory = models.CharField(max_length=50, choices=STUDENT_LABEL)
	subject = models.ManyToManyField(Subjects)

	def __str__(self):
		return f'{self.first_name}{self.last_name}'

class Teacher(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length= 2)
	address = models.CharField(max_length= 100)
	telephone = models.IntegerField()
	subject = models.ManyToManyField(Subjects)



	def __str__(self):
			return self.first_name




	