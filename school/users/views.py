from django.shortcuts import render

def login(request):
	return render(request, 'users/login.html')


def profile(request):
	return render(request, 'users/profile.html', {'tag': 'Profile Page'})