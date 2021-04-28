from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import reviews
from.forms import reviewsForm
# Create your views here.


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


@login_required
def update_review(request, reviews_id):
    reviews_being_updated = get_object_or_404(reviews, pk=reviews_id)
    if request.method == "POST":
        reviews_Form = reviewsForm(
            request.POST, instance=reviews_being_updated)

        if reviews_Form.is_valid():
            reviews_Form.save()
            messages.success(
                request, f"review from {reviews_Form .cleaned_data['name']} updated")
            return redirect(reverse(index))

        else:

            return render(request, 'reviews/create-template.html', {
                'form': reviews_Form
            })

    else:
        reviews_Form = reviewsForm(
            instance=reviews_being_updated)
        return render(request, 'reviews/update-template.html', {
            "form": reviews_Form
        })


@login_required
def delete_reviews(request, reviews_id):
    review_to_delete = get_object_or_404(reviews, pk=reviews_id)
    if request.method == 'POST':
        review_to_delete.delete()
        return redirect(index)
    else:
        return render(request, 'reviews/delete-template.html', {
            'reviews': review_to_delete
        })
