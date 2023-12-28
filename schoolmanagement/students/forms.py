from django import forms
from .models import Student, Address, Contact


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'suffix', 'birth_date',
                  'country_of_birth', 'birth_place', 'nationality', 'civil_status',
                  'sex', 'religion', 'mobile_number', 'telephone_number', 'personal_email']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'suffix': forms.TextInput(attrs={'class': 'form-control'}),
            'country_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'civil_status': forms.Select(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'religion': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'personal_email': forms.EmailInput(attrs={'class': 'form-control'}),

        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['province', 'city', 'house_number', 'barangay', 'postal_code']

        widgets = {
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'house_number':forms.TextInput(attrs={'class': 'form-control'}),
            'barangay': forms.TextInput(attrs={'class':'form-control'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'relationship']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'})
        }