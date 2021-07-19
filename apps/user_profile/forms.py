from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.shortcuts import get_object_or_404

username_validator = UnicodeUsernameValidator()



class UserRegistrationForm(UserCreationForm):
  first_name = forms.CharField(
    max_length=12, 
    min_length=4, 
    required=True, 
    help_text='Required: First Name',
    widget=forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'Bill'})
  )

  last_name = forms.CharField(
    max_length=12, 
    min_length=4, 
    required=True, 
    help_text='Required: Last Name',
    widget=(forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'Gates'}))
  )

  email = forms.EmailField(
    max_length=50, 
    help_text='Required. Enter a valid email address.',
    widget=(forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'bill.gates@microsoft.com'}))
  )
  
  password1 = forms.CharField(
    label=_('Password'),
    widget=(forms.PasswordInput(attrs={'class': 'input form-control'})),
    help_text=password_validation.password_validators_help_text_html()
  )
  
  password2 = forms.CharField(
    label=_('Password Confirmation'), 
    widget=forms.PasswordInput(attrs={'class': 'input form-control'}), help_text=_('Enter the same password as before, for verification.')
  )

  username = forms.CharField(
    label=_('Username'),
    max_length=150,
    help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    validators=[username_validator],
    error_messages={'unique': _("A user with that username already exists.")},
    widget=forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'bill.gates'})
  )

  class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)




class UserLoginForm(AuthenticationForm):
  username = forms.CharField(
    label=_('Username'),
    required=True,
    max_length=150,
    widget=forms.TextInput(attrs={'class': 'input form-control', 'placeholder': ''})
  )

  password = forms.CharField(
    label=_('Password'),
    required=True,
    max_length=150,
    widget=(forms.PasswordInput(attrs={'class': 'input form-control'})),
  )

  class Meta:
    model = User
    fields = '__all__'




class UserProfileForm(forms.ModelForm):
  first_name = forms.CharField(
    max_length=50, 
    required=True,
    widget=forms.TextInput(attrs={'class': 'input'})
  )

  last_name = forms.CharField(
    max_length=50, 
    required=True,
    widget=forms.TextInput(attrs={'class': 'input'})
  )

  email = forms.EmailField(
    max_length=50, 
    required=True,
    widget=forms.TextInput(attrs={'class': 'input'})
  )

  avatar = forms.ImageField(
    required=False,
    widget=forms.FileInput(attrs={'class': 'input form-control file-input', 'name': 'resume', 'accept': 'images/*'})
  )
  
  class Meta:
    model = UserProfile
    fields = ['first_name', 'last_name', 'avatar', 'email']