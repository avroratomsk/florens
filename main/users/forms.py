from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
  """Форма для аутентификации на сайте(логинться)"""
  username = forms.CharField()
  password = forms.CharField()
  
  class Meta:
    model = User
    fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
  first_name = forms.CharField()
  last_name = forms.CharField()
  email = forms.CharField()
  username = forms.CharField()
  password1 = forms.CharField()
  password2 = forms.CharField()
  
  class Meta:
    model = User
    fields = ("first_name", "last_name", "username", "email", "password1", "password2",)
    
 
