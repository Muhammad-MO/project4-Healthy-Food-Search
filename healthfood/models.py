from django.db import models
from pyuploadcare.dj.models import ImageField


# Create your models here.


class Maker(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):

        return self.name


class healthfood(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ingredients = models.CharField(blank=False, max_length=255)
    country = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    image = ImageField(blank=True, manual_crop="")
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    serving = models.TextField(blank=False)
    nutrition_carbs = models.CharField(blank=False, max_length=255)
    nutrition_protein = models.CharField(blank=False, max_length=255)
    nutrition_fats = models.CharField(blank=False, max_length=255)

    def __str__(self):

        return self.title
