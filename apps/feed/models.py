from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
  body = models.CharField(max_length=255)

  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created_at',)

  def __str__(self):
    return f"{self.created_by}'s tweet"