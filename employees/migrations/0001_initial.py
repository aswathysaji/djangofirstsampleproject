# Generated by Django 3.1 on 2020-09-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Available_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email_id', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=13)),
                ('employee_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('employee_address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('employee_job', models.ManyToManyField(blank=True, to='employees.Available_jobs')),
            ],
        ),
    ]