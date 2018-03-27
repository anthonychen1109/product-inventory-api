from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import viewsets
from . import models
from serializers import Product_Serializer, Inventory_Serializer
from rest_framework.response import Response

# Create your views here.
class Products_list(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = Product_Serializer

class Inventory_list(viewsets.ModelViewSet):
    queryset = models.Inventory.objects.all()
    serializer_class = Inventory_Serializer
