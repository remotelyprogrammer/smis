from django.contrib import admin
from .models import Instructor, Contact, Address

admin.site.register(Instructor)
admin.site.register(Address)
admin.site.register(Contact)
