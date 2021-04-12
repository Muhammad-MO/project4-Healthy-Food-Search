from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.


class healthfood(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    image = ImageField(blank=True, manual_crop="")


def __str__(self):

    return self.title
