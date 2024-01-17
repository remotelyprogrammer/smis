from django.db import models
from students.models import Student


# Tuition Fee Model
class TuitionFee(models.Model):
    grade_level = models.ForeignKey('academics.GradeLevel', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    academic_year = models.CharField(max_length=20)  # e.g. 2023-2024

    def __str__(self):
        return f"{self.grade_level.level} - {self.academic_year}"


# Billing Record Model
class BillingRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tuition_fee = models.ForeignKey(TuitionFee, on_delete=models.CASCADE)
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def is_paid(self):
        return self.amount_paid >= self.tuition_fee.amount

    def __str__(self):
        return f"{self.student} - {self.academic_year}"


# Payment Model
class Payment(models.Model):
    billing_record = models.ForeignKey(BillingRecord, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.billing_record.student} - {self.date}"
