from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False,
                            unique=True)
    amount_in_stock = models.IntegerField()

    def __str__(self):
        return self.name
