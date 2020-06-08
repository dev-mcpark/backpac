import re

from allauth.account.adapter import DefaultAccountAdapter
from django import forms


class MyAccountAdapter(DefaultAccountAdapter):
    def clean_password(self, password):
        if re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$', password):
            return password
        else:
            raise forms.ValidationError("Error message")
