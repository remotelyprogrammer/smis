from django.db import models

from students.models import Student

class Enrollment(models.Model):
    student_id = models.CharField(max_length=50)  # The unique ID of the student
    enrollment_date = models.DateField()

    ENROLLMENT_TYPE_CHOICE = [
        ('returning','Returning'),
        ('transferree', 'Transferree'),
    ]

    enrollment_type = models.CharField(max_length=50, choices=ENROLLMENT_TYPE_CHOICE, blank=True)
    def __str__(self):
        return f"Enrollment of student ID: {self.student_id}"

    def get_student_details(self):
        # Retrieve student details based on the student_id
        try:
            student = Student.objects.get(std_sch_id=self.student_id)
            return student
        except Student.DoesNotExist:
            return None