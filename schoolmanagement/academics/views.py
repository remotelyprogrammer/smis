from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import InstructorForm, SchoolYearForm, GradeLevelForm, SubjectForm
from .models import Instructor, SchoolYear, GradeLevel, Subject
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def add_instructor(request):
    if request.method == 'POST':
        instructor_form = InstructorForm(request.POST)
        if instructor_form.is_valid():
            user = instructor_form.save()  # Assuming the InstructorForm saves a User instance
            title = instructor_form.cleaned_data.get('title')
            department = instructor_form.cleaned_data.get('department')
            Instructor.objects.create(user=user, title=title, department=department)
            # Redirect to a new URL:
            return redirect('academics:academics_index')  # Replace with the name of your list view

    # if a GET (or any other method) we'll create a blank form
    else:
        instructor_form = InstructorForm()

    context = {
        'instructor_form': instructor_form,
        'page_heading': 'Instructor Registration'
    }
    print(instructor_form)
    return render(request, 'academics/add_instructor.html', context)


def academics_index(request):
    return render(request, 'academics/academics_index.html')


def instructor_login2(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page.
            return redirect('academics:academics_index')
    else:
        form = AuthenticationForm()
    return render(request, 'academics/instructors_login.html', {'form': form})


def instructor_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Check if the user is an instructor and redirect accordingly
            try:
                instructor = Instructor.objects.get(user=user)
                return redirect('academics:instructor_detail', instructor_id=instructor.pk)
            except Instructor.DoesNotExist:
                # Redirect to a default page if the user is not an instructor
                return redirect('students:list_student')
    else:
        form = AuthenticationForm()
    return render(request, 'academics/instructors_login.html', {'form': form})


def instructor_logout(request):
    logout(request)
    # Redirect to the login page (or any other page)
    return redirect('academics:instructor_login')


def instructor_detail(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    return render(request, 'academics/instructor_detail.html', {'instructor': instructor})

def add_school_year(request):
    if request.method == 'POST':
        form = SchoolYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academics:academics_index')
    else:
        form = SchoolYearForm()
    
    context = {
        'form':form,
    }

    return render(request, 'academics/add_sch_year.html', context)

def view_school_year(request, school_year_id):
    school_year = get_object_or_404(SchoolYear, pk=school_year_id)
    form = SchoolYearForm(instance=school_year)

    
    context = {
        'school_year': school_year,
        'form': form
    }
    
    return render(request, 'academics/view_school_year.html', context)

def list_school_year(request):
    school_years = SchoolYear.objects.all()
    context = {
        'school_years': school_years,
    }
    return render(request, 'academics/list_school_year.html', context)

def add_grade_level(request):
    if request.method == 'POST':
        form = GradeLevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academics:academics_index')
    else:
        form = GradeLevelForm()
    
    context = {
        'form':form,
    }

    return render(request, 'academics/add_grade_level.html', context)

def view_grade_level(request, grade_level_id):
    grade_level = get_object_or_404(GradeLevel, pk=grade_level_id)
    form = GradeLevelForm(instance=grade_level)

    
    context = {
        'grade_level': grade_level,
        'form': form
    }
    
    return render(request, 'academics/view_grade_level.html', context)

def list_grade_levels(request):
    grade_levels = GradeLevel.objects.all()
    context = {
        'grade_levels': grade_levels,
    }
    return render(request, 'academics/list_grade_levels.html', context)

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('academics:academics_index')
    else:
        form = SubjectForm()
    
    context = {
        'form':form,
    }

    return render(request, 'academics/add_subject.html', context)

def view_subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    form = SubjectForm(instance=subject)

    
    context = {
        'subject': subject,
        'form': form
    }
    
    return render(request, 'academics/view_subject.html', context)

def list_subjects(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, 'academics/list_subjects.html', context)