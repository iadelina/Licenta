from django import forms
from .models import RFIDKeysModel
from django.contrib.admin import widgets


class AddRFIDKeysForm(forms.Form):
    key = forms.CharField(label="Cheie Acces", max_length=13, required=False, widget=forms.TextInput(attrs={'placeholder': 'eg.9181823604798'}))
