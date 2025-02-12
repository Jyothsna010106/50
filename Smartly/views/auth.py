from django.shortcuts import render
from Smartly.models import Course , Video
from django.shortcuts import HttpResponse

def signup(request): 
    return render(request,
    template_name="Smartly/signup.html")

def login(request): 
    return render(request,
    template_name="Smartly/login.html")

                   