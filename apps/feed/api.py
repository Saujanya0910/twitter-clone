import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

from apps.notification.utilities import create_notification
import re

@login_required
def api_add_tweet(request):
  data = json.loads(request.body)  # convert json to python dict
  body = data['body']

  tweet = Tweet.objects.create(body=body, created_by=request.user)

  # use regex pattern check to see if any username is mentioned
  results = re.findall('(^|[^@\w])@(\w{1,20})', body)

  for result in results:
    result = result[1]
    # if actual user found, send notif for mention
    if User.objects.filter(username=result).exists() and result != request.user:
      create_notification(request, User.objects.get(username=result), 'mention')

  return JsonResponse({'success': True})


@login_required
def api_add_like(request):
  data = json.loads(request.body)  # convert json to python dict
  tweet_id = data['tweet_id']

# if like is present and liked by the current user
  if not Like.objects.filter(tweet_id=tweet_id).filter(created_by=request.user).exists():
    like = Like.objects.create(tweet_id=tweet_id, created_by=request.user)
    
    # get tweet details
    tweet = Tweet.objects.get(id=tweet_id)
    # send notif for like
    if  tweet.created_by != like.created_by:
      create_notification(request, tweet.created_by, 'like')

  return JsonResponse({'success': True})