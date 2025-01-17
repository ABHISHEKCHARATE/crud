# Generated by Django 4.2.13 on 2024-05-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('serial_number', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('section', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
