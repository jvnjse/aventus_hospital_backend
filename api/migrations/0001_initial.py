# Generated by Django 5.0.6 on 2024-06-30 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('contact_information', models.CharField(max_length=255)),
                ('medical_history', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('doctor_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('reason_for_visit', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient')),
            ],
        ),
    ]
