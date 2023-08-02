from django.http import HttpResponse
from django.shortcuts import render
from it_pojmy.models import ItPojem, Clanek, Kategorie, Komentar


def index(request):
    return render(request, 'it_pojmy/index.html')


def seznam(request):
    all_pojmy = ItPojem.objects.all()
    return render(request, 'it_pojmy/seznam.html', context={'all_pojmy': all_pojmy})


def detail(request, zkratka):
    return HttpResponse('TOTO JE DETAIL ' + zkratka)


# --------------------------------------------------

def seznam_clanku(request):
    clanky = Clanek.objects.order_by('-id')[:100]
    return render(
        request,
        'it_pojmy/clanek_list.html',
        context={'clanky': clanky}
    )


from django.views.generic import ListView


class ClanekList(ListView):
    model = Clanek
    context_object_name = 'clanky'
    paginate_by = 24


# clanky = Clanek.objects.all()
# clanky = Clanek.objects.filter(slug='ahoj')
# clanek = Clanek.objects.get(slug='ahoj', id=2)


def detail_clanku(request, slug_url):
    # slug = 'test-clanek-1/1/'
    # slug = 'test-clanek-1/2/'
    clanek = Clanek.objects.get(slug=slug_url)
    return render(
        request,
        'it_pojmy/clanek_detail.html',
        context={'clanek': clanek}
    )

def load_data2(request):
    for i in range(1000):
        Clanek.objects.update_or_create(
            slug = f'test-clanek-{i}',
            defaults = {'nazev': f'Test článek{i}'},
        )
        print(i)
    return HttpResponse('Data loaded')