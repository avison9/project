from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	D_O_B = models.DateTimeField()
	address = models.CharField()
	student_class = models.IntegerField()
	student_club = models.CharField()


	def fullname(self, first_name, last_name):
		return f'{self.first_name}{self.last_name}'


	def __str__(self):
		return self.fullname()

class Teacher(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	