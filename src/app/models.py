from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    quantity_on_hand = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

class Inventory(models.Model):
    pid = models.ForeignKey(Product)
    sum = models.DecimalField(max_digits=1000, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return str(self.pid)
