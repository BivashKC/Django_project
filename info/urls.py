from django.urls import path
from .views import *

app_name = 'info'


urlpatterns = [
    path('',homeview, name='home' ),
    path('contact-us',contactview, name='contact' ),
    path('notices',noticeview, name='notices' ),

]
