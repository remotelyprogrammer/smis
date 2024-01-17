from django.db import models
from django.contrib.auth.models import User


# Instructor Model
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # e.g., Dr., Mr., Ms.
    department = models.CharField(max_length=100)

    def __str__(self):
        user: User = self.user  # Type hint for IDE
        return f"{self.title} {self.user.first_name} {self.user.last_name}"


# Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


# Grade Level Model
class GradeLevel(models.Model):
    level = models.CharField(max_length=50) # e.g., Grade 1, Grade 2, etc.

    def __str__(self):
        return self.level


# Strand Model (specific to Senior High School in the Philippines)
class Strand(models.Model):
    name = models.CharField(max_length=100) # e.g., HUMSS, STEM, etc.
    description = models.TextField()

    def __str__(self):
        return self.name


# Class Model
class Classroom(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, null=True, blank=True)
    strand = models.ForeignKey(Strand, on_delete=models.CASCADE, null=True, blank=True)
    schedule = models.CharField(max_length=100) # This can be improved with a more complex schedule model

    def __str__(self):
        return f"{self.subject.name} - {self.instructor.user.last_name}"
