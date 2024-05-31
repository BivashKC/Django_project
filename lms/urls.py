from django.urls import path
from .views import *

app_name = 'lms'

urlpatterns = [
    path('courses', courseview, name='course'),
    path('notes', note_view, name='notes'),
    path('note-detail/<int:nid>', note_detail, name='note-detail'),
    path('note-update/<int:nid>', note_update, name='note-update'),
    path('note-delete/<int:nid>', note_delete, name='note-delete'),

]