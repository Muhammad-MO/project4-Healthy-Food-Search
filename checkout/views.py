
from django.shortcuts import render, reverse, HttpResponse, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
# import settings so that we can access the public stripe key
from django.conf import settings
import stripe
from healthfood.models import healthfood
from django.contrib.sites.models import Site


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('shopping_cart', {})
    line_items = []
    all_healthfood_ids = []

    for healthfood_id, item in cart.items():
        healthfoods = get_object_or_404(healthfood, pk=healthfood_id)

        item = {

            "name": healthfoods.title,
            "amount": int(healthfoods.cost * 100),
            "currency": "SGD",
            "quantity": item['qty']

        }

        line_items.append(item)

        all_healthfood_ids.append(str(healthfoods.id))

    current_site = Site.objects.get_current()

    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_healthfood_ids": "," .join(all_healthfood_ids)

        },
        mode="payment",
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")

    )

    return render(request, 'checkout/checkout-template.html', {

        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY

    })


@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        handle_payment(session)

    return HttpResponse(status=200)


def checkout_success(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout success")


def checkout_cancelled(request):
    # Empty the shopping cart
    request.session['shopping_cart'] = {}
    return HttpResponse("Checkout success")
