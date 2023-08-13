from django.urls import path
from eshop.views import (
    index,
    kategorie,
    kategorie_detail,
    znacka,
    produkt,
)


app_name = 'eshop'

urlpatterns = [
    path('', index, name='index'),
    path('kategorie/', kategorie, name='kategorie'),
    path('<slug:slug>/', kategorie_detail, name='kategorie_detail'),
    path('znacka/<slug:slug>/', znacka, name='znacka'),
    path('p/<slug:slug>/<int:pk>/', produkt, name='produkt'),
]