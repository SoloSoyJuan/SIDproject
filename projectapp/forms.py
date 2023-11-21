from django import forms
from .models import Customer


class CustomerForm(forms. ModelForm):

    class Meta:
        model=Customer
        fields=['customerId', 
                'firstName', 
                'lastName', 
                'address', 
                'dateOfBirth', 
                'email', 
                'homePhone', 
                'cellPhone']
        
        widgets = {
            'dateOfBirth': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(),
        }