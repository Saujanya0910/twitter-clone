from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required  # allow only if user is logged in
def feed(request):
  return render(request, 'feed/feed.html')