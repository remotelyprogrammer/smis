from django.shortcuts import render, redirect
from django.db import transaction
from .forms import InstructorForm, AddressForm, ContactForm
from django.contrib import messages

def index_instructor(request):
    return render(request, 'instructor/index.html')

def create_instructor(request):
    if request.method == 'POST':
        instructor_form = InstructorForm(request.POST)
        address_form = AddressForm(request.POST)
        contact_form = ContactForm(request.POST)

        if instructor_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
            with transaction.atomic():
                instructor = instructor_form.save()

                # Save address information
                address = address_form.save(commit=False)
                address.instructor = instructor
                address.save()

                # Save contact information
                contact = contact_form.save(commit=False)
                contact.instructor = instructor
                contact.save()

                messages.success(request, 'Instructor information saved successfully!')
                return redirect('instructors:index-instructor')  # Update the redirect URL

        else:
            # Handle form errors
            for form in [instructor_form, address_form, contact_form]:
                for error in form.errors.values():
                    messages.error(request, error)

    else:
        instructor_form = InstructorForm()
        address_form = AddressForm()
        contact_form = ContactForm()

    context = {
        'instructor_form': instructor_form,
        'address_form': address_form,
        'contact_form': contact_form,
        'page_heading': 'Instructor Registration'
    }
    return render(request, 'instructor/create-instructor.html', context)

