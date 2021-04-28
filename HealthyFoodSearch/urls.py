"""HealthyFoodSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import healthfood.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('healthfood/', healthfood.views.landing, name="show_healthfood_route"),
    path('', healthfood.views.index, name="show_landing_route"),
    path('reviews/', reviews.views.index, name='view_reviews_route'),
    path('healthfood/create/', healthfood.views.create_healthfood),
    path('healthfood/update/<healthfood_id>',
         healthfood.views.update_healthfood,  name="update_healthfood_route"),
    path('healthfood/delete/<healthfood_id>',
         healthfood.views.delete_healthfood, name='delete_healthfood_route'),
    path('reviews/create/',
         reviews.views.create_reviews, name='create_reviews_route'),
    path('reviews/update/<reviews_id>', reviews.views.update_review,
         name='update_reviews_route'),
    path('success/', healthfood.views.landing, name="show_healthfood_route"),
    path('view/<healthfood_id>', healthfood.views.view_healthfood_details,
         name='view_healthfood_details'),
    path('reviews/delete/<reviews_id>',
         reviews.views.delete_reviews, name='delete_reviews_route'),
    path('cart/', include('cart.urls'))

]
