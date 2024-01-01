from django import forms
from .models import Student, Address, Contact
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'suffix', 'birth_date',
                  'country_of_birth', 'birth_place', 'nationality', 'civil_status',
                  'sex', 'religion', 'mobile_number', 'telephone_number', 'personal_email']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Birthdate'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'First Name' }),
            'middle_name': forms.TextInput(attrs={'class': 'form-control','id': 'floatingInput', 'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Last Name'}),
            'suffix': forms.TextInput(attrs={'class': 'form-control','id': 'floatingInput', 'placeholder': 'Suffix'}),
            'country_of_birth': forms.TextInput(attrs={'class': 'form-control','id': 'floatingInput', 'placeholder': 'Country of Birth'}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Place of Birth'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Nationality'}),
            'civil_status': forms.Select(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Civil Status'}),
            'sex': forms.Select(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Sex'}),
            'religion': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Religion'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Mobile Number'}),
            'telephone_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Telephone Number'}),
            'personal_email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Personal Email'}),

        }

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['middle_name'].label = "Middle Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['suffix'].label = "Suffix"
        self.fields['country_of_birth'].label = "Country of Birth"
        self.fields['birth_place'].label = "Place of Birth"
        self.fields['nationality'].label = "Nationality"
        self.fields['civil_status'].label = "Civil Status"
        self.fields['religion'].label = "Religion"
        self.fields['mobile_number'].label = "Mobile No."
        self.fields['telephone_number'].label = "Telephone No."
        self.fields['personal_email'].label = "Personal E-mail"
        self.fields['sex'].label = "Sex"
        self.fields['birth_date'].label = "Birthdate"


class ViewStudentDetail(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'suffix', 'birth_date',
                  'country_of_birth', 'birth_place', 'nationality', 'civil_status',
                  'sex', 'religion', 'mobile_number', 'telephone_number', 'personal_email']
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Birthdate', 'disabled': 'disabled'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'First Name', 'disabled': 'disabled'}),
            'middle_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Middle Name', 'disabled': 'disabled'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Last Name', 'disabled': 'disabled'}),
            'suffix': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Suffix', 'disabled': 'disabled'}),
            'country_of_birth': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Country of Birth', 'disabled': 'disabled'}),
            'birth_place': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Place of Birth', 'disabled': 'disabled'}),
            'nationality': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Nationality', 'disabled': 'disabled'}),
            'civil_status': forms.Select(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Civil Status', 'disabled': 'disabled'}),
            'sex': forms.Select(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Sex', 'disabled': 'disabled'}),
            'religion': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Religion', 'disabled': 'disabled'}),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Mobile Number', 'disabled': 'disabled'}),
            'telephone_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Telephone Number', 'disabled': 'disabled'}),
            'personal_email': forms.EmailInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Personal Email', 'disabled': 'disabled'}),

        }


class EditStudentDetail(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'suffix', 'birth_date',
                  'country_of_birth', 'birth_place', 'nationality', 'civil_status',
                  'sex', 'religion', 'mobile_number', 'telephone_number', 'personal_email']
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Birthdate', }),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'First Name', }),
            'middle_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Middle Name', }),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Last Name', }),
            'suffix': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Suffix', }),
            'country_of_birth': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Country of Birth', }),
            'birth_place': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Place of Birth', }),
            'nationality': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Nationality', }),
            'civil_status': forms.Select(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Civil Status', }),
            'sex': forms.Select(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Sex', }),
            'religion': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Religion', }),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Mobile Number', }),
            'telephone_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Telephone Number', }),
            'personal_email': forms.EmailInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Personal Email', }),

        }


class ViewAddressDetail(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['province', 'city', 'house_number', 'barangay', 'postal_code']

        widgets = {
            'province': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'barangay': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['province', 'city', 'house_number', 'barangay', 'postal_code']

        widgets = {
            'province': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Province'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'City'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'House Number'}),
            'barangay': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Barangay'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Postal Code'}),
        }


class EditAddressDetail(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['province', 'city', 'house_number', 'barangay', 'postal_code']

        widgets = {
            'province': forms.TextInput(attrs={'class': 'form-control', }),
            'city': forms.TextInput(attrs={'class': 'form-control', }),
            'house_number': forms.TextInput(attrs={'class': 'form-control', }),
            'barangay': forms.TextInput(attrs={'class': 'form-control', }),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'relationship', 'mobile_number']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ViewContactDetail(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'relationship', 'mobile_number']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Mobile Number',
                       'disabled': 'disabled'}),
        }


class EditContactDetail(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'relationship', 'mobile_number']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', }),
            'relationship': forms.TextInput(attrs={'class': 'form-control', }),
            'mobile_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Mobile Number',
                       }),
        }
