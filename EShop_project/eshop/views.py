from django.shortcuts import render
from eshop.models import Kategorie


def index(request):
    all_pojmy = Kategorie.objects.all()
    return render(request, 'eshop/index.html', context={'all_pojmy':  all_pojmy})
