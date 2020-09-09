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
	gender = models.CharField(max_length= 6)
	# D_O_B = models.DateField(auto_now=False)
	address = models.CharField(max_length=300)
	parent_contact = models.CharField(max_length=11)
	student_class = models.CharField(max_length= 10)
	student_club = models.CharField(max_length=100)
	# student_catergory = models.CharField(max_length=50, choices=STUDENT_LABEL)
	subject = models.ManyToManyField(Subjects, through='Related')

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Teacher(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	gender = models.CharField(max_length= 6)
	address = models.CharField(max_length= 100)
	telephone = models.CharField(max_length=11)
	subject = models.ManyToManyField(Subjects)

	def __str__(self):
			return self.first_name



class Related(models.Model):
	subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
	students = models.ForeignKey(Student, on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	ca_1 = models.CharField(max_length= 2, blank=True)
	ca_2 = models.CharField(max_length=2, blank=True)
	exam_grade = models.CharField(max_length=2, blank=True, null=True)
	final_grade = models.CharField(max_length=3, blank=True, null=True)
	enroll_date = models.DateField(auto_now=False)