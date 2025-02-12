from django.shortcuts import render , redirect
from Smartly.models import Course , Video
from django.shortcuts import HttpResponse

def coursePage(request,slug):
     
     course= Course.objects.get(slug=slug) 
     serial_number=request.GET.get('lecture')
     videos=course.video_set.all().order_by("serial_number")

     if serial_number is None:
          serial_number=1
     video = Video.objects.get(serial_number = serial_number , course = course)
     print("priview video",video.is_preview)
     
     if((request.user.is_authenticated is False) and (video.is_preview is False)):
          return redirect("login")
     
     #if you r enrolled  then u can watch every video


     print(video)
     context={
          "course":course,
          "video":video,
          'videos':videos
     }
     return render(request,template_name="Smartly/course_page.html", context=context)

                   