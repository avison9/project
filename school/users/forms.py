from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
	firstname = forms.CharField()
	lastname = forms.CharField()
	address = forms.CharField()
	Student_club = forms.CharField()
	


	class Meta:
		model = User
		fields = ['username', 'email','password1','password2']