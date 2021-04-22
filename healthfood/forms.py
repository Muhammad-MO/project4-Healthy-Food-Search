from django import forms
from .models import healthfood
from pyuploadcare.dj.forms import ImageField


class healthfoodForm(forms.ModelForm):

    class Meta:
        image = ImageField(label='')

        model = healthfood
        fields = ('title', 'description', 'ISBN', 'image', 'maker')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
