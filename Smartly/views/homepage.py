from django.shortcuts import render
from Smartly.models import Course
from django.shortcuts import HttpResponse


def home(request):
    Smartly = Course.objects.all()
    print(Smartly)



    return render(request,template_name="Smartly/home.html",
                  context={"Smartly":Smartly} ) 