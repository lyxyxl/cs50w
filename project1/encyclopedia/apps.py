from django.apps import AppConfig
from django import forms


class EncyclopediaConfig(AppConfig):
    name = 'encyclopedia'

class SearchForm(forms.Form):
    q = forms.CharField(max_length=64)