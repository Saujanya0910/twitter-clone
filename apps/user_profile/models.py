from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)  # if A follows B, B should not automatically follow back A
  avatar = models.ImageField(upload_to='uploads/', blank=False, null=False)
  # , default='uploads/default.jpg'

  def __str__(self):
    return f"{self.user.username} - profile"


# handle user obj on a new signup, by either creating new or checking for existing one and using it
User.user_profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])