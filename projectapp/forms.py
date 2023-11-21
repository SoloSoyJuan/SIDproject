from django import forms
from .models import Customers


class CustomerForm(forms. ModelForm):

    class Meta:
        model=Customers
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