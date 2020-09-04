from django.db import models
from django.contrib.auth.models import User 
from model_utils import Choices

class Senior_Student(models.Model):
	SUBJECTS = Choices(
		('Mathematics',_('Mathematics')),
		('English',_('English Language')),
		('Physics',_('Physics')),
		('Chemistry',_('Chemistry')),
		('Biology',_('Biology')),
		('Geography',_('Geography')),
		('Accounts',_('Financial Accounting')),
		('Commerce',_('Commerce')),
		('Literature',_('Literature in English')),
		('FMath',_('Further Mathematics'))
	)
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	D_O_B = models.DateTimeField()
	address = models.CharField(max_length=300)
	student_class = models.IntegerField()
	student_club = models.CharField(max_length=100)
	subject = models.CharField(max_length=50, choices=SUBJECTS)


	def __str__(self):
		return f'{self.first_name}{self.last_name}'

class Teacher(models.Model):
	username = models.ManyToManyFields()


	class Meta:
		model = Student
		fields = ['first_name','last_name','address','subject']

	