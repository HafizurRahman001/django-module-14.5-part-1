from django import forms
from .models import contactModelForm

class contactForm(forms.ModelForm):
    class Meta:
        model = contactModelForm
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : "Student Roll",
            'address':'Write your address'
        }
        widgets  = {
            'name' : forms.TextInput(),
            'date_field': forms.TextInput(attrs={'type':'date'}),
            'date_time_field':forms.DateInput(attrs= {'type' : 'datetime-local'})
        }
        help_texts = {
            'name' : "Write your full name",
            'roll' : "Write your Roll Number",
            'address' : "Write your address",
            'decimal_field' : "maximum digits=5 and decimal places=2",
            'float_field' : "Enter any float number",
            'integer_Number':"Enter only integer number"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }