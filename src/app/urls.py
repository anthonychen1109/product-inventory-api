from django.conf.urls import url
from .views import Products_list

urlpatterns = [
    url(r'^$', Products_list.as_view(), name="products_list"),
]
