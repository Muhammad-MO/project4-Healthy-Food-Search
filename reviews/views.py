from django.shortcuts import render, HttpResponse
from .models import reviews

# Create your views here.


def index(request):
    all_reviews = reviews.objects.all()
    return render(request, 'reviews/index-template.html', {
        'reviews': all_reviews
    })
