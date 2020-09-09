from django.db import models
from django.contrib.auth.models import User 
from model_utils import Choices

class Student(models.Model):
	STUDENT_LABEL = Choices(
		('Senior Class',('Senior Catergory'))
		('Junior',('Junior Catergory'))
		)
	username = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length= 100)
	last_name = models.CharField(max_length= 100)
	gender = models.CharField(max_length= 2)
	D_O_B = models.DateTimeField()
	address = models.CharField(max_length=300)
	parent_contact = models.IntegerField()
	student_class = models.IntegerField()
	student_club = models.CharField(max_length=100)
	student_catergory = models.CharField(max_length=50, choices=STUDENT_LABEL)

	def __str__(self):
		return f'{self.first_name}{self.last_name}'

class Teacher(models.Model):
	telephone = models.IntegerField()

	class Meta:
		model = Student
		fields = ['username','first_name','last_name','gender','address']


	def __str__(self):
			return self.first_name

class Subjects(models.Model):
	subject = model.CharField(max_length=100)

	def __str__(self):
		return self.subject


	