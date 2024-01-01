from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class InstructorForm(UserCreationForm):
    title = forms.CharField(max_length=100, required=True)
    department = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('title', 'department')