from django.shortcuts import render
from Smartly.models import Course , Video
from django.shortcuts import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def signup(request): 
    if(request.method =="GET"):
      form = UserCreationForm()
      return render(request,
      template_name="Smartly/signup.html ", context= { 'form' : form })
    
    return HttpResponse("POST REQUEST")

def login(request): 
    return render(request,
    template_name="Smartly/login.html")

                   