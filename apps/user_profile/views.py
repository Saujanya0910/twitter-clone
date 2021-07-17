from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *
from apps.notification.utilities import create_notification

# Create your views here.
def user_profile(request, username):
  user = get_object_or_404(User, username=username)

  tweets = user.tweets.all()
  for tweet in tweets:
    likes = tweet.likes.filter(created_by_id=request.user.id)

    if likes.count() > 0:
      tweet.liked = True
    else:
      tweet.liked = False

  context = {
    'user': user,
    'tweets': tweets
  }

  return render(request, 'user_profile/user_profile.html', context)


@login_required
def edit_profile(request):
  if request.method == 'POST':
    form = UserProfileForm(request.POST, request.FILES, instance=request.user.user_profile)

    if form.is_valid():
      form.save()
      return redirect('user_profile', username=request.user.username)

  else:
    form = UserProfileForm(instance=request.user.user_profile)

  context = {
    'user': request.user,
    'form': form
  }

  return render(request, 'user_profile/edit_profile.html', context)

@login_required
def follow_user(request, username):
  user = get_object_or_404(User, username=username)

  # add user to following list
  request.user.user_profile.follows.add(user.user_profile)

  # send notification for a new follower
  create_notification(request, user, 'follower')

  return redirect('user_profile', username=username)


@login_required
def unfollow_user(request, username):
  user = get_object_or_404(User, username=username)

  # remove user from following list
  request.user.user_profile.follows.remove(user.user_profile)

  return redirect('user_profile', username=username)


def followers(request, username):
  user = get_object_or_404(User, username=username)

  return render(request, 'user_profile/followers.html', {'user': user})


def followings(request, username):
  user = get_object_or_404(User, username=username)

  return render(request, 'user_profile/following.html', {'user': user})