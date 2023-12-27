from django.contrib import admin
from .models import Student, Address, Contact

# Register your models here.
admin.site.register(Student)
admin.site.register(Address)
admin.site.register(Contact)