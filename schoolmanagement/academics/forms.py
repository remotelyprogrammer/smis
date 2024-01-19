from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import SchoolYear, GradeLevel, Subject


# class InstructorForm(UserCreationForm):
#     title = forms.CharField(max_length=100, required=True)
#     department = forms.CharField(max_length=100, required=True)

#     class Meta:
#         model = User
#         fields = UserCreationForm.Meta.fields + ('title', 'department')

class SchoolYearForm(forms.ModelForm):
    class Meta:
        model = SchoolYear
        fields = '__all__'

class GradeLevelForm(forms.ModelForm):
    class Meta:
        model = GradeLevel
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'