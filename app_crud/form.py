# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser , Employee , Manager

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee  # Replace 'Employee' with your actual Employee model name
        fields = ['serial_number', 'name', 'mobile', 'salary', 'location', 'job_role']


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['name', 'mobile', 'salary', 'section', 'project_name', 'department']