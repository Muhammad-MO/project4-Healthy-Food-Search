from django.contrib import admin
from django.urls import path, include
import checkout.views


urlpatterns = [
    path('', checkout.views.checkout, name='checkout'),
    path('success', checkout.views.checkout_success, name="checkout_success"),
    path('cancelled', checkout.views.checkout_cancelled, name="checkout_cancelled"),
    path('payment_completed', checkout.views.payment_completed)
]
