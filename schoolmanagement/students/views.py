from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, AddressForm, ContactForm
from django.contrib import messages
from django.db import transaction


def blank(requests):
    context = {'page_heading': 'Blank Page Heading'}
    return render(requests, 'students/blank.html', context)


def register_student2(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST)
        address_form = AddressForm(request.POST)
        contact_form = ContactForm(request.POST)
        if all([student_form.is_valid(), address_form.is_valid(), contact_form.is_valid()]):
            student = student_form.save()
            address = address_form.save(commit=False)
            address.student = student  # Assuming a OneToOne relation
            address.save()
            contact = contact_form.save(commit=False)
            contact.student = student  # Assuming a ForeignKey relation
            contact.save()
            return redirect('students:students-home')
    else:
        student_form = StudentRegistrationForm()
        address_form = AddressForm()
        contact_form = ContactForm()
    context = {
        'student_form': student_form,
        'address_form': address_form,
        'contact_form': contact_form,
        'page_heading': 'Student Registration'
    }

    return render(request, 'students/register_student.html', context)


def register_student(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST)
        address_form = AddressForm(request.POST)
        contact_form = ContactForm(request.POST)

        # Check if all forms are valid
        if student_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
            with transaction.atomic():  # Ensure that all objects are saved or none if there's an error
                student = student_form.save()
                address = address_form.save(commit=False)
                address.student = student
                address.save()
                contact = contact_form.save(commit=False)
                contact.student = student
                contact.save()
                messages.success(request, 'Student, address, and contact information saved successfully!')
                return redirect('students:students-home')  # Adjust the redirect to the correct URL name
        else:
            # If forms are not valid, add the error messages
            for error in student_form.errors.values():
                messages.error(request, error)
            for error in address_form.errors.values():
                messages.error(request, error)
            for error in contact_form.errors.values():
                messages.error(request, error)
    else:
        student_form = StudentRegistrationForm()
        address_form = AddressForm()
        contact_form = ContactForm()

    context = {
        'student_form': student_form,
        'address_form': address_form,
        'contact_form': contact_form,
        'page_heading': 'Student Registration'
    }

    return render(request, 'students/register_student2.html', context)
