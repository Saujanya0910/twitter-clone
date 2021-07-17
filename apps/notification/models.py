from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
  MESSAGE = 'message'
  FOLLOWER = 'follower'
  LIKE = 'like'
  MENTION = 'mention'

  CHOICES = (
    (MESSAGE, 'Message'),
    (FOLLOWER, 'Follower'),
    (LIKE, 'Like'),
    (MENTION, 'Mention'),
  )

  to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
  notification_type = models.CharField(max_length=20, choices=CHOICES)
  is_read = models.BooleanField(default=False)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notification_creator')
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.notification_type} for {self.to_user.username}" 