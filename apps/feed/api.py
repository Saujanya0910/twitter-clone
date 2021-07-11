import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def api_add_tweet(request):
  data = json.loads(request.body)  # convert json to python dict
  body = data['body']

  tweet = Tweet.objects.create(body=body, created_by=request.user)

  return JsonResponse({'success': True})