from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm

def login(request):
  if request.method == "POST":
    form = UserLoginForm(data=request.POST)
    if form.is_valid:
      username = request.POST["username"]
      password = request.POST["password"]
      user = auth.authenticate(username=username, password=password)
      if user:
        auth.login(request, user)
        return HttpResponseRedirect(reverse("home"))
  else:
    form = UserLoginForm()
  
  context = {
    "title": "Страница авторизации",
    "form":form,
  }
  
  return render(request, 'pages/users/login.html', context)

def register(request):
  if request.method == "POST":
    form = UserRegistrationForm(data=request.POST)
    if form.is_valid:
      form.save()
      user = form.instance
      auth.login(request, user)
      return HttpResponseRedirect(reverse("home"))
  else:
    form = UserRegistrationForm()
    
  context = {
    "title": "Страница регистрации",
    "form": form
  }
  
  return render(request, 'pages/users/register.html', context)

def profile(request):
  context = {
    "title": "Личный кабинет",
  }
  
  return render(request, 'pages/users/profile.html', context)

def logout(request):
  pass