from .views import blank
from django.urls import path


app_name = 'students'

urlpatterns = [
    path('', blank, name='students-blank'),
]