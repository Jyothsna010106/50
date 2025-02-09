from django.contrib import admin
from django.urls import path , include
from Smartly.views import home 
from django.conf.urls.static import static
from codejj.settings import MEDIA_ROOT,MEDIA_URL


urlpatterns = [
    path('',home,name='home' ),
 
] + static(MEDIA_URL, document_root= MEDIA_ROOT)
