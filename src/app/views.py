from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

# Create your views here.

class ProductList(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class InventoryList(viewsets.ModelViewSet):
    queryset = models.Inventory.objects.all()
    serializer_class = serializers.InventorySerializer
