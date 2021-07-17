from .models import *

def create_notification(request, to_user, notification_type):
  Notification.objects.create(
    to_user=to_user,
    notification_type=notification_type,
    created_by=request.user
  )