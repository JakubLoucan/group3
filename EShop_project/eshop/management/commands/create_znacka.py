from django.core.management.base import BaseCommand
from eshop.models import Znacka


class Command(BaseCommand):
    def handle(selg, *args, **options):
        print("Command is called")
        path = 'eshop/management/data/znacka.txt'
        with open(path, encoding='UTF-8') as soubor:
            for radek in soubor:
                print("vytvorena znacka")
                Znacka.objects.update_or_create(nazev=radek)







