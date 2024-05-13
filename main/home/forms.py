from django import forms
from home.models import HomeTemplate
from shop.models import Category,Product
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class CallbackForm(forms.Form):
  name = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваше имя',
      'class': 'form__controls'
      }
  ))

  phone = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      }
  ))
  
  message = forms.CharField(min_length=2, widget=forms.Textarea(
    attrs={
      'placeholder': 'Ваше сообщение',
      'class': 'form__controls',
      'rows': 7
      }
  ))
  # captcha = ReCaptchaField()
  
class QuickOrderForm(forms.Form):
  
  name = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваше имя',
      'class': 'form__controls'
      }
  ))

  phone = forms.CharField(min_length=2, widget=forms.TextInput(
    attrs={
      'placeholder': 'Ваш номер телефона',
      'class': 'form__controls'
      }
  ))
  
  goods = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Продукт',
      'class': 'form__controls',
      'type': 'hidden',
      }
  ))