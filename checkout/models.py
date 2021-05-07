from healthfood.models import healthfood
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Purchase(models.Model):
    healthfood_id = models.ForeignKey(healthfood, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase made for healthfood#{self.healthfood_id} by user#{self.user_id} on {self.purchase_date}"
