__author__ = 'Alkesh'
from django import forms

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL')