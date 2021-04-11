from django.db import models

# Create your models here.


class healthfood(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)


def __str__(self):

    return self.title
