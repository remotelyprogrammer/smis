from django.urls import path
from .views import create_instructor, index_instructor

app_name = 'instructors'

urlpatterns = [
        path('', index_instructor, name='index-instructor'),
        path('create/', create_instructor, name='create-instructor'),
    
]