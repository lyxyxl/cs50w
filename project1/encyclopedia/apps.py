from django.apps import AppConfig
from django import forms


class EncyclopediaConfig(AppConfig):
    name = 'encyclopedia'

class SearchForm(forms.Form):
    q = forms.CharField(max_length=64)

class CreateForm(forms.Form):
    title = forms.CharField(max_length=64)
    content = forms.CharField(widget=forms.Textarea)

class EditForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)