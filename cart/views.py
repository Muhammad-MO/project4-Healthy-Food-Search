from django.shortcuts import render,  get_object_or_404, redirect, reverse
from django.contrib import messages

from healthfood.models import healthfood


# Create your views here.


def add_to_cart(request, healthfood_id):
    cart = request.session.get('shopping_cart', {})

    # we check if the healthfood_is not in the cart. If so, we will add it

    healthfoods = get_object_or_404(healthfood, pk=healthfood_id)
    # healthfood is found, let's add it to the cart

    if healthfood_id in cart:
        cart[healthfood_id]['qty'] += 1
        cart[healthfood_id]['total_cost'] = int(
            cart[healthfood_id]['qty']) * float(cart[healthfood_id]['cost'])

    else:

        cart[healthfood_id] = {

            'title': healthfoods.title,
            'cost': float(healthfoods.cost),
            'qty': 1
        }

    # save the cart back to sessions
    request.session['shopping_cart'] = cart

    messages.success(request, "Item has been added to your cart!")
    return redirect(reverse("show_healthfood_route"))


def views_cart(request):
    cart = request.session.get('shopping_cart', {})

    return render(request, 'cart/view_cart-template.html', {
        'cart': cart

    })


def remove_from_cart(request, healthfood_id):
    cart = request.session.get('shopping_cart', {})

    if healthfood_id in cart:
        del cart[healthfood_id]
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart!")
        return redirect(reverse('views_cart'))


# def update_quantity(request, healthfood_id):
    # cart = request.session.get('shopping_cart')
    # if healthfood_id in cart:
      #  cart[healthfood_id]['qty'] = request.POST['qty']
      #  request.session['shopping_cart'] = cart
      # 3 messages.success(request, 'The quantity for the item has changed')
    # return redirect(reverse('views_cart'))
