from django.shortcuts import render , redirect
from Smartly.models import Course , Video , UserCourse
from django.shortcuts import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='login') , name='dispatch')
class MyCoursesList(ListView):
    template_name = 'Smartly/my_courses.html'
    context_object_name = 'user_courses'
    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)


def coursePage(request , slug):
    course = Course.objects.get(slug  = slug)
    serial_number  = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    next_lecture=2

    if serial_number is None:
        serial_number = 1 
    else:
        next_lecture=int(serial_number)+1

    video = Video.objects.get(serial_number = serial_number , course = course)

    if (video.is_preview is False):

        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user  , course = course)
            except:
                return redirect("check-out" , slug=course.slug)
        
        
    context = {
        "course" : course , 
        "video" : video , 
        'videos':videos,
        "next_lecture":next_lecture
    }
    return  render(request , template_name="Smartly/course_page.html" , context=context )    
    