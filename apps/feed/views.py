from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

@login_required  # allow only if user is logged in
def feed(request):
  userids = [request.user.id]
  
  # to get all follower's ids
  for author in request.user.userprofile.follows.all():
    userids.append(author.user.id)

  # get all tweets for those ids
  tweets = Tweet.objects.filter(created_by_id__in=userids)

  return render(request, 'feed/feed.html', {'tweets': tweets})