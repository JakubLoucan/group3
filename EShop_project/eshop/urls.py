from django.urls import path
from eshop.views import (
    index,
    kategorie_list,
    kategorie_detail,
    znacka_detail,
    produkt_detail,
)


app_name = 'eshop'

urlpatterns = [
    path('', index, name='index'),
    path('kategorie/', kategorie_list, name='kategorie'),
    path('<slug:slug>/', kategorie_detail, name='kategorie_detail'),
    path('znacka/<slug:slug>/', znacka_detail, name='znacka_detail'),
    path('p/<slug:slug>/<int:pk>/', produkt_detail, name='produkt_detail'),
]
