from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpadteForm, ProfileUpadteForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('blog-home')
	else:
		form = UserRegistrationForm();
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	
	if request.method == 'POST':
		u_form = UserUpadteForm(request.POST, instance = request.user)
		p_form = ProfileUpadteForm(request.POST, request.FILES, instance = request.user.profile)
		context = {
			'u_form': u_form,
			'p_form': p_form
		}
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'User Profile Updated Successfully!')
			return redirect('profile')
	else:
		u_form = UserUpadteForm(instance = request.user)
		p_form = ProfileUpadteForm(instance = request.user.profile)
		context = {
			'u_form': u_form,
			'p_form': p_form
		}
	return render(request, 'users/profile.html', context)