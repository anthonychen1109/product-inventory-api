from rest_framework import serializers
from .models import Product, Inventory

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Inventory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
