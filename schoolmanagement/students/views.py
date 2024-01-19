from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentRegistrationForm, AddressForm, ContactForm, \
    ViewAddressDetail, ViewContactDetail, ViewStudentDetail, \
    EditStudentDetail, EditAddressDetail, EditContactDetail

from django.contrib import messages
from django.db import transaction
from .models import Student, Contact, Address
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def blank(requests):
    context = {'page_heading': 'Blank Page Heading'}
    return render(requests, 'students/blank.html', context)


def read_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    # Assuming a OneToOne relationship with Address
    address = Address.objects.filter(student=student).first()
    address_form = ViewAddressDetail(instance=address)

    # Assuming a ForeignKey relationship with Contact (fetching all related contacts)
    contacts = Contact.objects.filter(student=student)
    contact_form = [ViewContactDetail(instance=contact) for contact in contacts]

    context = {
        'student_form': ViewStudentDetail(instance=student),
        'address_form': address_form,
        'contact_form': contact_form,
        'student_id': student_id,
        'page_heading': 'Student Detail'
    }
    return render(request, 'students/read-student.html', context)


def create_student(request):
    if request.method == 'POST':
        student_form = StudentRegistrationForm(request.POST)
        address_form = AddressForm(request.POST)
        contact_form = ContactForm(request.POST)

        if student_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
            with transaction.atomic():
                student = student_form.save()

                # Save address information
                address = address_form.save(commit=False)
                address.student = student
                address.save()

                # Save contact information
                contact = contact_form.save(commit=False)
                contact.student = student
                contact.save()

                messages.success(request, 'Student information saved successfully!')
                return redirect('students:students-home')
        else:
            # Handle form errors
            for form in [student_form, address_form, contact_form]:
                for error in form.errors.values():
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
    return render(request, 'students/create-student.html', context)


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    address = Address.objects.filter(student=student).first()
    contacts = Contact.objects.filter(student=student)

    if request.method == 'POST':
        student_form = EditStudentDetail(request.POST, instance=student)
        address_form = EditAddressDetail(request.POST, instance=address)
        contact_forms = [EditContactDetail(request.POST, instance=contact) for contact in contacts]

        if (student_form.is_valid() and address_form.is_valid()
                and all(cf.is_valid() for cf in contact_forms)):
            student_form.save()
            address_form.save()
            for cf in contact_forms:
                cf.save()
            messages.success(request, 'Student details updated successfully!')
            return redirect('students:students-home')
        else:
            # Print form errors to the console
            print("Student Form Errors:", student_form.errors)
            print("Address Form Errors:", address_form.errors)
            for cf in contact_forms:
                print("Contact Form Errors:", cf.errors)

    else:
        student_form = StudentRegistrationForm(instance=student)
        address_form = AddressForm(instance=address)
        contact_forms = [ContactForm(instance=contact) for contact in contacts]

    return render(request, 'students/update-student.html', {
        'student_form': student_form,
        'address_form': address_form,
        'contact_form': contact_forms,
        'student_id': student_id,
    })


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    messages.success(request, 'Student record deleted successfully!')
    return HttpResponseRedirect(reverse('students:students-home'))


def list_students(request):
    students = Student.objects.all()
    for student in students:
        print(student.first_name)
    context = {
        'students': students,
        'page_heading': 'Student List',
    }
    return render(request, 'students/list-students.html', context)