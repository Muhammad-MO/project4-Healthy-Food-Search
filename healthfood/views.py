from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import healthfood
from.forms import healthfoodForm

# Create your views here.


def index(request):
    all_healthfood = healthfood.objects.all()
    return render(request, 'healthfood/index-template.html', {
        'healthfood': all_healthfood
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

    if request.method == "POST":
        healthfood_being_updated = get_object_or_404(
            healthfood, pk=healthfood_id)
        healthfood_Form = healthfoodForm(
            request.POST, instance=healthfood_being_updated)

        if healthfood_Form.is_valid():
            healthfood_Form.save()
        return redirect(reverse(index))

    else:
        healthfood_being_updated = get_object_or_404(
            healthfood, pk=healthfood_id)

        healthfood_Form = healthfoodForm(instance=healthfood_being_updated)
        return render(request, 'healthfood/update-template.html', {
            "form": healthfood_Form
        })


def delete_healthfood(request, healthfood_id):
    delete_healthfood = get_object_or_404(healthfood, pk=healthfood_id)
    return render(request, 'healthfood/delete-template.html', {
        "healthfood": delete_healthfood
    })
