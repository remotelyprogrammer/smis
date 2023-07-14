from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=10, blank=True)
    birth_date = models.DateField()
    country_of_birth = models.CharField(max_length=100)
    birth_place = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    civil_status = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    religion = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=20, blank=True)
    personal_email = models.EmailField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"


class Address(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    barangay = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.house_number} {self.barangay}, {self.city}, {self.province}"


class Contact(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='contacts')
    full_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=20)

    def __str__(self):
        return self.name