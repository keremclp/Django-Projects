from django.forms import forms

def min_lenght_3(value):
    if len(value) < 3 :
        raise forms.ValidationError('Title must be greater than 3 characters')