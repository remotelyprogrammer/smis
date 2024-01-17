from django.contrib import admin
from .models import Instructor, Classroom, Subject, GradeLevel, Strand

# Register your models here.
admin.site.register(Instructor)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(GradeLevel)
admin.site.register(Strand)