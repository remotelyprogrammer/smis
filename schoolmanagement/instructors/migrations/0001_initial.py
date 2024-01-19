# Generated by Django 5.0 on 2024-01-19 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ins_sch_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('suffix', models.CharField(blank=True, max_length=10)),
                ('birth_date', models.DateField()),
                ('country_of_birth', models.CharField(max_length=100)),
                ('birth_place', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('civil_status', models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced'), ('separated', 'Separated')], max_length=20)),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('religion', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=20)),
                ('telephone_number', models.CharField(blank=True, max_length=20)),
                ('personal_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(blank=True, max_length=20)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='instructors.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=20)),
                ('barangay', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('instructor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='instructors.instructor')),
            ],
        ),
    ]
