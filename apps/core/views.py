from django.shortcuts import render

# Create your views here.
def frontpage(request):
  return render(request, 'core/frontpage.html')


def login(request):
  return render(request, 'core/login.html')


def signup(request):
  return render(request, 'core/signup.html')