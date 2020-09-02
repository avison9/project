from django.db import models
from django.contrib.auth.models import User 

class Student(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	D_O_B = models.DateTimeField()
	address = models.CharField(max_length=300)
	student_class = models.IntegerField()
	student_club = models.CharField(max_length=100)
	


	def fullname(self, first_name, last_name):
		return f'{self.first_name}{self.last_name}'


	def __str__(self):
		return self.fullname()

class Teacher(models.Model):

	