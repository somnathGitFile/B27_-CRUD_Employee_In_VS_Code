from dataclasses import fields
from pyexpat import model
from django import forms
from.models import Emplyee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Emplyee
        fields = '__all__'

        labels = {
            'eid':'Employee Id',
            'name':'Employee Name',
            'mail': 'Email',
            'sal': 'Salary',
            'address': 'Address'
        }

        widgets ={
            'eid': forms.NumberInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Enter Employee ID',
            })
        }