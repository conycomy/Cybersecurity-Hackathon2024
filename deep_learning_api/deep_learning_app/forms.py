# forms.py
from django import forms

class InputForm(forms.Form):
    text_input = forms.CharField(label='Enter text', max_length=100)
