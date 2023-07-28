from django.db import models

class ItPojem(models.Model):
    zkratka = models.SlugField(max_length=100)
    nazev = models.CharField(max_length=100)
    popis = models.CharField(max_length=500, blank=True)

class Clanek(models.Model):
    slug = models.SlugField(max_length=100)
    nazev = models.CharField(max_length=100)
    obsah = models.CharField(max_length=1000, blank=True)
