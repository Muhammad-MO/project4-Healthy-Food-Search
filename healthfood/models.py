from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name


class healthfood(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    image = ImageField(blank=True, manual_crop="")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):

        return self.title
