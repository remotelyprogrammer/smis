from django.urls import path
from .views import index

app_name = 'webutil'

urlpatterns = [
    path('', index, name='index-webutil'),

]