from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)  # if A follows B, B should not automatically follow back A

# handle user obj on a new signup, by either creating new or checking for existing one and using it
User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])