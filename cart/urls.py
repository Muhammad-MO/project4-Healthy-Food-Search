from django.urls import path
import cart.views


urlpatterns = [
    path('add_to_cart/<healthfood_id>', cart.views.add_to_cart, name='add_to_cart')
]
