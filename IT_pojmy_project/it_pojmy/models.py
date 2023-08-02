from django.db import models

"""
DB tabulka ItPojem

    ^
    |
    *

Django Model:
ItPojem
    zkratka
    nazev
    popis

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
"""


class ItPojem(models.Model):
    zkratka = models.SlugField(max_length=100)
    nazev = models.CharField(max_length=100)
    popis = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.nazev


class Kategorie(models.Model):
    slug = models.SlugField(max_length=100)
    nazev = models.CharField(max_length=100)

class Komentar(models.Model):
    autor = models.SlugField(max_length=100)
    obsah = models.CharField(max_length=500)





# /test-clanek-1/98897/
# /test-clanek-1/17171/

class Clanek(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    nazev = models.CharField(max_length=100)
    popis = models.CharField(max_length=500, blank=True)
    datum = models.DateTimeField(blank=True, null=True)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.PROTECT, blank=True, null=True)
    komentar = models.ForeignKey(Komentar, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        return self.nazev

