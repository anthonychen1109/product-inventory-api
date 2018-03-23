from django.conf.urls import url
from .views import products_list

urlpatterns = [
    url(r'^$', products_list),
]
