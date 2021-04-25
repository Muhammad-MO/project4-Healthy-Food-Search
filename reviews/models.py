from django.db import models
import datetime
from healthfood.models import healthfood

# Create your models here.


class reviews(models.Model):
    name = models.CharField(blank=False, max_length=255)
    Email = models.EmailField(blank=False, max_length=320)
    date = models.DateField(default=datetime.date.today)
    reviews = models.TextField(blank=False)
    healthfood = models.ForeignKey(healthfood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
