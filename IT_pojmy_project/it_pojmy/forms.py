from django import forms
from it_pojmy.models import Clanek

"""
# info
Tvorba formulářů ručně (občas se může hodit, pokud opravdu potřebujete custom formulář)
https://docs.djangoproject.com/en/4.2/topics/forms/
Tvorba formulářů pro daný model
https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/
"""


# info: Vytváříme Django formulář, který se stará o zpracování fomrmuláře (reprezentuje samotný formulář)
# info: Formulář také zajístí validaci odeslaných informací (např datové typy, délku, povinnosti ...)
class ClanekForm(forms.ModelForm):
    class Meta:
        model = Clanek  # musíme určit, který model řeší
        fields = ['slug', 'nazev', 'popis', 'kategorie']  # musíme učit, která pole může uživatel editovat