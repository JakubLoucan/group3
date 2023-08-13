from django.shortcuts import render, reverse
from eshop.models import Kategorie


def index(request):
    return render(request, 'eshop/index.html')


def kategorie(request):
    object_list = Kategorie.objects.all()
    return render(request, 'eshop/kategorie.html', context={'object_list': object_list})


def kategorie_detail(request, slug):
    object_detail = Kategorie.objects.get(slug=slug)
    return render(request, 'eshop/kategorie_detail.html', context={'object_detail': object_detail})


def znacka(request, slug):
    return render(request, 'eshop/znacka.html')


def produkt(request, slug, pk):
    return render(request, 'eshop/produkt.html')