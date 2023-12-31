# forms.py
from django import forms
from grh.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nom_emp', 'preno_emp', 'daten_emp', 'adre_emp']
