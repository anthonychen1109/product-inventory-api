from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=False, default="")
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    quantity_on_hand = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    pid = models.ForeignKey(Product, on_delete=models.CASCADE)
    sum = models.DecimalField(decimal_places=2, max_digits=1000)

    def __str__(self):
        return self.pid
