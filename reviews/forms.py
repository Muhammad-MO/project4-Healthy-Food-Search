from django import forms
from .models import reviews


class reviewsForm(forms.ModelForm):
    class Meta:

     model = reviews
     fields = ('name', 'Email', 'date', 'reviews')
