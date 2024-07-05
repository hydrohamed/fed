from django import forms
from .models import FloodEvent


class FloodEventFilterForm(forms.Form):
    start_datetime_from = forms.DateTimeField(
        required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    start_datetime_to = forms.DateTimeField(
        required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    type = forms.ChoiceField(
        choices=[('', 'All')] + FloodEvent.TYPE_CHOICES, required=False)
    cause = forms.ChoiceField(
        choices=[('', 'All')] + FloodEvent.CAUSE_CHOICES, required=False)
    severity = forms.ChoiceField(
        choices=[('', 'All')] + FloodEvent.SEVERITY_CHOICES, required=False)
