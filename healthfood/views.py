from django.shortcuts import render
from .models import healthfood

# Create your views here.


def index(request):
    all_healthfood = healthfood.objects.all()
    return render(request, 'healthfood/index-template.html', {
        'healthfood': all_healthfood
    })
