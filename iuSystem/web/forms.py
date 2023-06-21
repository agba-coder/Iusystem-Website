from django import forms
from django.forms import ModelForm
from .models import Participant

class RegistrationForm(ModelForm):
    image = forms.ImageField()
    # first_name = forms.CharField(widget=forms.CharField())
    class Meta:
        model = Participant
        fields = ["image"]
        