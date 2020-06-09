import re

from allauth.account.adapter import DefaultAccountAdapter
from django import forms


class MyAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super(MyAccountAdapter, self).save_user(request, user, form, commit)

        return user
