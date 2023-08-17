from django.shortcuts import render
from eshop.models import Kategorie, Znacka


def index(request):
    kategorie = Kategorie.objects.all()
    return render(request, 'eshop/index.html', context={'kategorie': kategorie})

# todo: předjmenovat views
"""
kategorie -> kategorie_list
znacka -> znacka_detail
produtk -> produkt_detail
"""


def kategorie_list(request):
    object_list = Kategorie.objects.all()
    return render(request, 'eshop/kategorie.html', context={'object_list': object_list})


def kategorie_detail(request, slug):
    kategorie = Kategorie.objects.get(slug=slug)
    return render(request, 'eshop/kategorie_detail.html', context={'kategorie': kategorie})


def znacka_detail(request, slug):
    detail = Znacka.objects.all(slug=slug)
    return render(request, 'eshop/znacka.html', context={'detail': detail})


def produkt_detail(request, slug, pk):
    return render(request, 'eshop/produkt.html')