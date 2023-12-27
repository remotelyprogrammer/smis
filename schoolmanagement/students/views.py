from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, AddressForm, ContactForm
from django.contrib import messages


def blank(requests):
    context = {'page_heading': 'Blank Page Heading'}
    return render(requests, 'students/blank.html', context)


def register_student(request):
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
