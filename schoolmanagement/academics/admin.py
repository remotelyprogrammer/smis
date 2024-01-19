from django.contrib import admin
from .models import Subject, GradeLevel, SchoolYear

# Register your models here.
admin.site.register(SchoolYear)
# admin.site.register(Instructor)
admin.site.register(Subject)
admin.site.register(GradeLevel)