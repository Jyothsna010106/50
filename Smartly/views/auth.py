from django.shortcuts import render , redirect
from Smartly.models import Course , Video
from django.shortcuts import HttpResponse



from Smartly.forms import RegistrationForm

def signup(request): 
    if(request.method =="GET"):
      form = RegistrationForm()
      return render(request,
      template_name="Smartly/signup.html ", context= { 'form' : form })
    
    form = RegistrationForm(request.POST)
    if(form.is_valid()):
      user = form.save()
      if(user is not None):
        return redirect('login')
    return render(request,
      template_name="Smartly/signup.html ", context= { 'form' : form })

def login(request): 
    return render(request,
    template_name="Smartly/login.html")

                   