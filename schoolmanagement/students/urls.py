from .views import blank, create_student, read_student, update_student, delete_student, list_students
from django.urls import path


app_name = 'students'

urlpatterns = [
    path('', blank, name='students-home'),
    path('create/', create_student, name='create-student'),
    path('read/<int:student_id>/', read_student, name='read-student'),
    path('update/<int:student_id>/', update_student, name='update-student'),
    path('delete/<int:student_id>/', delete_student, name='delete-student'),
    path('lists/', list_students, name='list-students'),

]