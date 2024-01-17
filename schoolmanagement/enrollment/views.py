from django.shortcuts import render, redirect, get_object_or_404
from .forms import EnrollmentForm
from students.models import Student
from .models import Enrollment

from django.http import HttpResponse

def register_enrollment(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or the list of enrollments
            return redirect('register_enrollment')  # Replace with your desired redirect
    else:
        form = EnrollmentForm()

    return render(request, 'enrollment/enroll.html', {'form': form})


def view_enrollee(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, pk=enrollment_id)
    student = enrollment.get_student_details()
    full_name = f"{student.first_name} {student.middle_name} {student.last_name}" if student else "Student not found"

    context = {
        'enrollment': enrollment,
        'student': student,
        'page_heading': f'Enrollment Details for Student ID: {enrollment.student_id}',
        'full_name' : full_name,
    }

    return render(request, 'enrollment/enrollee.html', context)

def list_enrollees(request):
    # student = get_object_or_404(Student, pk=enrollment_id)
    enrollments = Enrollment.objects.all()
    context = {
        'enrollments':enrollments
    }
    return render(request, 'enrollment/list-enrolls.html', {'enrollments': enrollments})