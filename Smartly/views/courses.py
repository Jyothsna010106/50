from django.shortcuts import render
from Smartly.models import Course
from django.shortcuts import HttpResponse


def coursePage(request,slug):
    
     course= Course.objects.get(slug=slug) 
     context={
          "course":course
     }
     return render(request,template_name="Smartly/course_page.html", context=context)

                   