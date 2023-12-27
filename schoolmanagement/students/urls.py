from .views import blank, register_student
from django.urls import path


app_name = 'students'

urlpatterns = [
    path('', blank, name='students-home'),
    path('register/', register_student, name='register_student')
]