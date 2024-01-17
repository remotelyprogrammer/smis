from django.urls import path
from .views import register_enrollment, view_enrollee, list_enrollees

app_name = 'enrollment'

urlpatterns = [
    path('register/', register_enrollment, name='register_enrollment'),
    path('view-enrollee/<int:enrollment_id>/', view_enrollee, name='view_enrollee'),
    path('list-enrollees/', list_enrollees, name='list_enrollees'),


]