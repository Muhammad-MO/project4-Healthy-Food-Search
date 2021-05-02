from django.db import models
from healthfood.models import healthfood


# Create your models here.

class cart(models.Model):

    name = models.CharField(blank=False, max_length=255)
    healthfood = models.ForeignKey(healthfood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
