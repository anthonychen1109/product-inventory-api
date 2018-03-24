from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

# Create your views here.
class Products_list(ListView):
    model = Product
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        product_list = super().get_context_data(**kwargs)
        return product_list
