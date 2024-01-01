from .views import academics_index, add_instructor, instructor_login, instructor_detail, instructor_logout
from django.urls import path


app_name = 'academics'

urlpatterns = [
    path('', academics_index, name='academics_index'),
    path('add_instructor/', add_instructor, name='add_instructor'),
    path('instructor/login/', instructor_login, name='instructor_login'),
    path('instructor/<int:instructor_id>/', instructor_detail, name='instructor_detail'),
    path('instructor/logout/', instructor_logout, name='instructor_logout'),
]