from django import forms
from .models import healthfood


class healthfoodForm(forms.ModelForm):
    class Meta:
        model = healthfood
        fields = ('title', 'description', 'ISBN')
        
