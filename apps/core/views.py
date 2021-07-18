from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.user_profile.forms import UserRegistrationForm

# Create your views here.
def frontpage(request):
  return render(request, 'core/frontpage.html')


def signup(request):

  if request.user.is_authenticated:
    return redirect('feed')

  # if logging in
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get('username')
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password1')

      user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        is_active=True
      )

      user.save()
      new_user = authenticate(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password1'],
      )
      login(request, new_user)

      return redirect('frontpage')
  
  # create a new user
  else:
    form = UserRegistrationForm()

  return render(request, 'core/signup.html', {'form': form})