from django import forms
import datetime

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput,initial='Your name')
    email = forms.EmailField(widget=forms.EmailInput,label="Please enter your email address",)
    comment = forms.CharField(widget=forms.Textarea)
    agree = forms.BooleanField()
    date = forms.DateField(initial=datetime.date.today,widget=forms.DateInput(attrs={'type':'date'}),)
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(
	    max_length = 10,
    )

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_colors = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_in_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_multiple = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

    first_name = forms.CharField(max_length = 200)  
    last_name = forms.CharField(max_length = 200)  
    roll_number = forms.IntegerField(  
                     help_text = "Enter 6 digit roll number"
                     )  
    file = forms.FileField()
    dateTime = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    check = forms.BooleanField()
    float_field = forms.FloatField()
    generic_ipaddress = forms.GenericIPAddressField( )
    null_boolean = forms.NullBooleanField( ) 


