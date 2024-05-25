# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=150, unique=True)
    
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    def __str__(self):
        return self.username


class Employee(models.Model):
    serial_number = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.serial_number}: {self.name}"
    


class Manager(models.Model):
    serial_number = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    section = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.serial_number}: {self.name}"
