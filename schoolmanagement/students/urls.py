from .views import blank, register_student, view_student, edit_student_details, delete_student, list_student
from django.urls import path


app_name = 'students'

urlpatterns = [
    path('', blank, name='students-home'),
    path('register/', register_student, name='register_student'),
    path('<int:student_id>/', view_student, name='view_student'),
    path('edit/<int:student_id>/', edit_student_details, name='edit_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
    path('list/', list_student, name='list_student'),

]