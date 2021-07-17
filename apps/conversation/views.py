from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


# view all conversations
@login_required
def conversations(request):
  conversations = request.user.conversations.all()  # all convos list

  return render(request, 'conversations/conversations.html', {'conversations': conversations})


# individual convo/chat with another user
@login_required
def conversation(request, user_id):
  # get all convos for the current user
  conversations = Conversation.objects.filter(users__in=[request.user.id])
  # check if convo exists with the selected user
  conversations = conversations.filter(users__in=[user_id])

  # check if convo exists, else create new one
  if conversations.count() == 1:
    conversation = conversations[0]
  else:
    recipient = User.objects.get(pk=user_id)
    conversation = Conversation.objects.create()

    conversation.users.add(request.user)
    conversation.users.add(recipient)
    conversation.save()

  return render(request, 'conversations/conversation.html', {'conversation': conversation})