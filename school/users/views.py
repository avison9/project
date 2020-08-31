from django.shortcuts import render
from .forms import UserRegistrationForm

def login(request):
	return render(request, 'users/login.html')


def profile(request):
	return render(request, 'users/profile.html', {'tag': 'Profile Page'})

def registration(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'{username}, profile has been created successfully!')
			return redirect('profile')
	else:
		form = UserRegistrationForm()
	context = {
		'tag':'Student Registration',
		'form': form
	}
	return render(request, 'users/registration.html', context)