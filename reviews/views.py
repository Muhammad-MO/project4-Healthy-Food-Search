from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import reviews
from.forms import reviewsForm
# Create your views here.

@login_required
def index(request):
    all_reviews = reviews.objects.all()
    return render(request, 'reviews/index-template.html', {
        'reviews': all_reviews

    })


@login_required
def create_reviews(request):
    if request.method == 'POST':
        create_form = reviewsForm(request.POST)

        if create_form.is_valid():
            create_form.save()

            messages.success(
                request, f"New review {create_form.cleaned_data['name']} has been created")

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
