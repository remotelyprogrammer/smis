from django.forms import modelform_factory
from .models import Instructor, Address, Contact

InstructorForm = modelform_factory(Instructor, fields='__all__')
AddressForm = modelform_factory(Address, exclude=('instructor',))
ContactForm = modelform_factory(Contact, exclude=('instructor',))