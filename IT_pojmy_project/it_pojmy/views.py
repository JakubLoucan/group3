from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from it_pojmy.models import ItPojem, Clanek, Komentar
from it_pojmy.forms import ClanekForm


def home(request):
    return render(request, 'it_pojmy/home.html')


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


class ClanekList(ListView):
    model = Clanek
    context_object_name = 'clanky'
    paginate_by = 24


def detail_clanku(request, slug_url):
    # slug = 'test-clanek-1/1/'
    # slug = 'test-clanek-1/2/'
    clanek = Clanek.objects.get(slug=slug_url)
    return render(
        request,
        'it_pojmy/clanek_detail.html',
        context={'clanek': clanek}
    )


def novy_komentar(request):
    # info: z post dat získáme požadované informace
    clanek_id = request.POST['clanek_id']
    autor = request.POST['autor']
    obsah = request.POST['obsah']

    # info: podle těchto dat vytvoříme komentář
    Komentar.objects.create(
        autor=autor,
        obsah=obsah,
        clanek_id=clanek_id,
    )

    # info: najdeme článek, abychom ně něj mohli udělat redirect
    clanek = Clanek.objects.get(id=clanek_id)

    return redirect(
        reverse('it_pojmy:detail_clanku', kwargs={'slug_url': clanek.slug})
    )


# info: zde náš formulář napojíme na View, to view dokáže formulář jak vykreslit tak zpracovat
# info: stačí pak jen definovat template a url cestu, na které formulář bude
class ClanekCreateView(CreateView):
    form_class = ClanekForm
    template_name = 'it_pojmy/clanek_form.html'