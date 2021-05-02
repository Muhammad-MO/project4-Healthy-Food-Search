from django.urls import path
import cart.views


urlpatterns = [
    path('add/<healthfood_id>',
         cart.views.add_to_cart, name='add_to_cart'),
    path('', cart.views.views_cart, name='views_cart'),
    path('remove/<healthfood_id>',
         cart.views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<healthfood_id>',
         cart.views.update_quantity, name='update_cart')


]
