from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# # Instructor Model
# class Instructor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100) # e.g., Dr., Mr., Ms.
#     department = models.CharField(max_length=100)

#     def __str__(self):
#         user: User = self.user  # Type hint for IDE
#         return f"{self.title} {self.user.first_name} {self.user.last_name}"

class SchoolYear(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"), blank=True)
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    is_current = models.BooleanField(default=False, verbose_name=_("Is Current School Year"))

    class Meta:
        verbose_name = _("School Year")
        verbose_name_plural = _("School Years")
        ordering = ['-start_date']  # Orders the school years starting with the most recent

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_current:
            # Ensure that there is only one current school year
            SchoolYear.objects.filter(is_current=True).update(is_current=False)
        super(SchoolYear, self).save(*args, **kwargs)


class GradeLevel(models.Model):
    name = models.CharField(_("Grade Level"), max_length=50, blank=True)
    school_year = models.ForeignKey(
        SchoolYear, 
        on_delete=models.CASCADE, 
        verbose_name=_("School Year"), 
        related_name='grade_levels'
    )

    class Meta:
        verbose_name = _("Grade Level")
        verbose_name_plural = _("Grade Levels")
        ordering = ['name']
        unique_together = ['name', 'school_year']

    def __str__(self):
        return f"{self.name} - {self.school_year.name}"


class Subject(models.Model):
    name = models.CharField(_("Subject Name"), max_length=255, blank=True)
    code = models.CharField(_("Subject Code"), max_length=10, unique=True)
    grade_level = models.ForeignKey(
        GradeLevel, 
        on_delete=models.CASCADE, 
        verbose_name=_("Grade Level"), 
        related_name='subjects'
    )
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.grade_level.name}"


# # Class Model
# class Classroom(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
#     grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, null=True, blank=True)
#     strand = models.ForeignKey(Strand, on_delete=models.CASCADE, null=True, blank=True)
#     schedule = models.CharField(max_length=100) # This can be improved with a more complex schedule model

#     def __str__(self):
#         return f"{self.subject.name} - {self.instructor.user.last_name}"
