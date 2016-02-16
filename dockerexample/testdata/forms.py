import logging

from django import forms


# Get an instance of a logger
log = logging.getLogger(__name__)


class DataForm(forms.Form):
    key = forms.CharField(
            required=True,
            widget=forms.TextInput(
                    attrs={'placeholder': 'Key',
                           'class': 'form-control'}),
            error_messages={'required': 'Key is required'})
    value = forms.CharField(
            required=True,
            widget=forms.TextInput(
                    attrs={'placeholder': 'Value',
                           'class': 'form-control'}),
            error_messages={'required': 'Value is required'})
