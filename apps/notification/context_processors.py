from .models import Notification

# to show notifications in the navbar
def notifications(request):
  if request.user.is_authenticated:
    return {'notifications': request.user.notifications.filter(is_read=False)}
  else:
    return {'notifications': []}