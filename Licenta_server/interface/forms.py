from django.forms import ModelForm
from .models import *
from django.contrib.admin import widgets
from django.utils.translation import gettext_lazy as _

class AddRFIDKeysForm(ModelForm):
    class Meta:
        model = RFIDKeysModel
        fields = ['key']
        labels = {
               'key':_('Cheie'),
        }
        # key = forms.CharField(label="Cheie Acces", max_length=13, required=False, widget=forms.TextInput(attrs={'placeholder': 'eg.9181823604798'}))

class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumberModel
        fields = ['number']
        labels = {
               'number':_('Numar'),
        }
