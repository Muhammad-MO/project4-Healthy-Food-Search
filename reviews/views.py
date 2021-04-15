from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import reviews
from.forms import reviewsForm
# Create your views here.


def index(request):
    all_reviews = reviews.objects.all()
    return render(request, 'reviews/index-template.html', {
        'reviews': all_reviews

    })


def create_reviews(request):
    if request.method == 'POST':
        create_form = reviewsForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:

            return render(request, 'reviews/create-template.html', {
                'form': create_form
            })

    else:
        create_form = reviewsForm()
        return render(request, 'reviews/create-template.html', {
            'form': create_form
        })
