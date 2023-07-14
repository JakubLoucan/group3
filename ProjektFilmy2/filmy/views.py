from django.shortcuts import render, HttpResponse, Http404
from django.http import JsonResponse
from django.shortcuts import reverse
from django.utils.text import slugify
from filmy.data import filmy_data
from filmy.data2 import herci_data

"""
Domácí úkol: samostatná práce - seznam herců + detail herce

0) mít data v dict
1) views.py
seznam_hercu -> return render() + html
detail_herce -> return render() + html

2) urls.py
/seznam-hercu/
-> /filmy/seznam-hercu/

/detail-herce/<slug:slug>/
-> /filmy/detail-herce/jim-carrey/

3) nedělat search!!!

---------------------------------------------------------------------------------------
Zamyšlení:
TODO: jak udělat vazby herec - film (přes dict data) ???
TODO: jak udělat kategorie filmů (přes dict data) ???
- namodelovat tyto věci v dict, ještě to nedělat do DB, to až příště
"""


def seznam(request):
    slug = slugify(request.GET.get('text', ''))
    if slug:
        data = {}
        for key_film in filmy_data:
            if key_film.startswith(slug):
                data[key_film] = filmy_data[key_film]

        context = {'filmy_data': data}
    else:
        context = {'filmy_data': filmy_data}
    return render(request, 'filmy/seznam.html', context=context)


def detail(request, slug):
    if slug in filmy_data:
        film = filmy_data[slug]
        response = render(request, 'filmy/detail.html', context={'film': film})
        response['MOJE-DATA'] = 'HELLO!'
        # response['Content-Type'] = 'application/json; charset=utf-8'
        return response
    else:
        raise Http404('Film nebyl nalezen')


def seznam_json(request):
    return JsonResponse(filmy_data)
from django.shortcuts import render

def seznam_hercu(request):
    return render(request, 'filmy/herci_seznam.html', context={'herci_data': herci_data})

def detail_herce(request, slug):
    if slug in herci_data:
        herec = herci_data[slug]
        return render(request, 'filmy/herci_popis.html', context={'herec': herec})

# Create your views here.
