from django import forms
from .models import Rewiews

class RewiewForm(forms.ModelForm):
    class Meta:
        model=Rewiews
        fields=("name","email","text")
        