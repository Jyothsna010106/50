# Code Citations

## License: unknown
https://github.com/feelfreetocodecourse/course-seeling-website-Django-/tree/6260e5f327f2fd88a7552f65643123ba4a3aaf27/courses/views/checkout.py

```
import *
from time import time
import razorpay

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

@login_required(login_url='/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = request
```


## License: unknown
https://github.com/pratikshete312/Blueleran-Courses-Website-/tree/9f4c2a71e9df4a324311349b5dd04838aadd0e2c/courses/views/checkout.py

```
, KEY_SECRET))

@login_required(login_url='/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('action')
    order = None
    payment
```


## License: unknown
https://github.com/kamalkant255/Lms/tree/39dc82eb3bf35e27f8a1e043fd972f37a4cae651/website/views/checkout.py

```
.Client(auth=(KEY_ID, KEY_SECRET))

@login_required(login_url='/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('
```


## License: unknown
https://github.com/ganeshpatil97/course-selling-website/tree/ce7fcfd57e7e44be23cf2722a28b2c787cab8557/courses/views/checkout.py

```
settings import *
from time import time
import razorpay

client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

@login_required(login_url='/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user =
```


## License: unknown
https://github.com/chvijaypatel/Course/tree/9befa1794351de38c2f2a55c5b72a0a99be15b23/main_app/views.py

```
/login')
def checkout(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    try:
        user_course = UserCourse
```

