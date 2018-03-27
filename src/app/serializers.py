from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inventory
        fields = "__all__"
