from django.shortcuts import render
from Smartly.models import Course
from django.shortcuts import HttpResponse


def coursePage(request,slug):
     print(slug)
     context={
          "slug":slug
     }
     return render(request,template_name="Smartly/course_page.html", context=context)

                   