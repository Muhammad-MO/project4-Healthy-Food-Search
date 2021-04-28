from django.shortcuts import render,  get_object_or_404, redirect, reverse
from django.contrib import messages

from healthfood.models import healthfood


# Create your views here.


def add_to_cart(request, healthfood_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})

    # we check if the book_is not in the cart. If so, we will add it
    if healthfood_id not in cart:
        healthfood_cart = get_object_or_404(healthfood, pk=healthfood_id)
        # book is found, let's add it to the cart
        cart[healthfood_id] = {
            'id': healthfood_id,
            'title': healthfood.title,
            'cost': 99,
            'qty': 1
        }

        # save the cart back to sessions
        request.session['shopping_cart'] = cart

        messages.success(request, "Item has been added to your cart!")
        return redirect(reverse("show_healthfood_route"))
    else:
        cart[healthfood_id]['qty'] += 1
        request.session['shopping_cart'] = cart
        return redirect(reverse("show_healthfood_route"))
