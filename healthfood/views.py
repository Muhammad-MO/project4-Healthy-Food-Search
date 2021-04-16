from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect, reverse

from django.shortcuts import get_object_or_404
from .models import healthfood
from.forms import healthfoodForm, SearchForm

# Create your views here.


def index(request):
    all_healthfood = healthfood.objects.all()

    if request.GET:
        # always true query:
        queries = ~Q(pk__in=[])

        # if a title is specified, add it to the query
        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            queries = queries & Q(title__icontains=title)

        all_healthfood = all_healthfood.filter(queries)

        search_form = SearchForm(request.GET)

    return render(request, 'healthfood/index-template.html', {
        'healthfood': all_healthfood,
        'search_form': SearchForm,

    })


def create_healthfood(request):
    if request.method == 'POST':  # 1
        create_form = healthfoodForm(request.POST)  # 2

        # check if the form has valid values
        if create_form.is_valid():  # 3
            create_form.save()  # 4
            return redirect(reverse(index))
        else:
            # 5. if does not have valid values, re-render the form
            return render(request, 'healthfood/create.template.html', {
                'form': create_form
            })
    else:
        create_form = healthfoodForm()
        return render(request, 'healthfood/create.template.html', {
            'form': create_form
        })


def update_healthfood(request, healthfood_id):
    healthfood_being_updated = get_object_or_404(healthfood, pk=healthfood_id)
    if request.method == "POST":
        healthfood_Form = healthfoodForm(
            request.POST, instance=healthfood_being_updated)

        if healthfood_Form.is_valid():
            healthfood_Form.save()
            return redirect(reverse(index))

        else:

            return render(request, 'healthfood/update-template.html', {
                "form": healthfood_Form
            })

    else:
        healthfood_Form = healthfoodForm(instance=healthfood_being_updated)
        return render(request, 'healthfood/update-template.html', {
            "form": healthfood_Form
        })


def delete_healthfood(request, healthfood_id):
    healthfood_to_delete = get_object_or_404(healthfood, pk=healthfood_id)
    if request.method == 'POST':
        healthfood_to_delete.delete()
        return redirect(index)

    else:

        return render(request, 'healthfood/delete-template.html', {
            'healthfood': healthfood_to_delete
        })
