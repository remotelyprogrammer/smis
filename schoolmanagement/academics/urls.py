from .views import academics_index, add_instructor, instructor_login, instructor_detail, instructor_logout, add_school_year, view_school_year, list_school_year, \
    add_grade_level, view_grade_level, list_grade_levels, add_subject, view_subject, list_subjects
from django.urls import path


app_name = 'academics'

urlpatterns = [
    path('', academics_index, name='academics_index'),
    path('add_instructor/', add_instructor, name='add_instructor'),
    path('instructor/login/', instructor_login, name='instructor_login'),
    path('instructor/<int:instructor_id>/', instructor_detail, name='instructor_detail'),
    path('instructor/logout/', instructor_logout, name='instructor_logout'),

    path('add_school_year/', add_school_year, name='add_school_year'),
    path('view_school_year/<int:school_year_id>/', view_school_year, name='view_school_year'),
    path('list_school_year/', list_school_year, name='list_school_year'),

    path('add_grade_level/', add_grade_level, name='add_grade_level'),
    path('view_grade_level/<int:grade_level_id>/', view_grade_level, name='view_grade_level'),
    path('list_grade_levels/', list_grade_levels, name='list_grade_levels'),

    path('add_subject/', add_subject, name='add_subject'),
    path('view_subject/<int:subject_id>/', view_subject, name='view_subject'),
    path('list_subjects/', list_subjects, name='list_subjects'),

]