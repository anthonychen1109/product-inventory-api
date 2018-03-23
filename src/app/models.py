from django.db import models

# Create your models here.
class Product(models.Model):
    price = models.DecimalField(null=False, blank=False)
    quantity_on_hand = models.PositiveIntegerField()

class Inventory(models.Model):
    id = models.ForeignKey(Product)
    sum = models.DecimalField()
