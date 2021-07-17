from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def notifications(request):
  goto = request.GET.get('goto', '')
  notification_id = request.GET.get('id', 0)

  if goto != '':
    notification = Notification.objects.get(id=notification_id)
    notification.is_read = True
    notification.save()

    if notification.notification_type == Notification.MESSAGE:
      return redirect('conversation', user_id=notification.created_by.id)
    elif notification.notification_type == Notification.FOLLOWER:
      return redirect('user_profile', username=notification.created_by.username)
    elif notification.notification_type == Notification.LIKE:
      return redirect('user_profile', username=notification.to_user.username)
    elif notification.notification_type == Notification.MENTION:
      return redirect('user_profile', username=notification.created_by.username)

  return render(request, 'notification/notifications.html')