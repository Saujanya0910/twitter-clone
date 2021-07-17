from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conversation(models.Model):
  users = models.ManyToManyField(User, related_name='conversations')
  modified_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-modified_at']

  def __str__(self):
    return f"{self.users} - conversation"



class ConversationMessages(models.Model):
  conversation = models.ForeignKey(Conversation, related_name='messages_conversation', on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, related_name='message_author', on_delete=models.CASCADE)

  class Meta:
    ordering = ['created_at']


  def save(self, *args, **kwargs):
    self.conversation.save()

    super(Conversation, self).save(*args, **kwargs)

  def __str__(self):
    return f"{self.created_by.username} - message"