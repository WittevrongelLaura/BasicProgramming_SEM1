# Oef 9
# Maak een python applicatie dat voor een groep personen (studenten/docenten) een
# snelheidscontrole in de straat ‘Graaf Karel de goedelaan’ simuleert.
# Stap 0: we starten met een een list met personeelsleden.
# list_personeel = ["Stijn", "Gilles", "Dieter", "Christophe"]
# Stap 1: als simulatie wordt voor elke persoon een willekeurige snelheid tussen 10 en 70km/u
# gegeneerd. Hiervoor gebruik je de functie ‘registreer_snelheidsmeting’. Het resultaat van
# deze functie is een dictionary. De key is het personeelslid, de value de willekeurige snelheid
# Stap 2: print alle snelheden per persoon af. Vermeld ook de straatnaam. Gebruik hiervoor een
# functie ‘print_snelheden_personen’
# Stap 3: vraag aan de gebruiker de maximum toegelaten snelheid in de betrokken straat.
# Stap 4: filter de overtredingen uit de dictionary. Gebruik hiervoor een afzonderlijke functie
# ‘filter_overtredingen’. Geef als parameter de startdictionary en de maximum toegelaten
# snelheid mee. Wat geef deze functie terug?
# Stap 5: print de boetes uit voor de overtredingen uit. De boete wordt als volgt berekend: 10€
# per km boven de toegelaten snelheid. Gebruik hiervoor opnieuw een afzonderlijke functie
# ‘print_boetes’
# Een voorbeeld:
# Geregistreerde snelheden in de straat Graaf Karel de goedelaan:
# Stijn 30 km/u
# Gilles 37 km/u
# Dieter 67 km/u
# Christophe 40 km/u
# Geef de maximum toegelaten snelheid op:> 30
# De te innnen boetes zijn:
# Gilles boete: 70€
# Dieter boete: 370€
# Christophe boete: 100€

import random

def registreer_snelheidsmeting(list_personen):
    dict_metingen = {}
    for persoon in list_personen:
        dict_metingen[persoon] = random.randint(10, 70)
    return dict_metingen

def print_snelheden_personen(dict):
    for naam, snelheid in dict.items():
        print(f"{naam:20}\t\t{snelheid} km/u")

def filter_overtredingen(dict_metingen, max_snel):
    dict_overtreders = {}
    for naam, snelheid in dict_metingen.items():
        if snelheid > max_snel:
            boete = (snelheid - max_snel) * 10
            dict_overtreders[naam] = boete
    return dict_overtreders

def print_boetes(dict):
    for persoon, boete in dict.items():
        print(f"{persoon:20}\t\tboete: {boete}€")

list_personeel = ["Stijn", "Gilles", "Dieter", "Christophe"]

dict_metingen = registreer_snelheidsmeting(list_personeel)

print_snelheden_personen(dict_metingen)

max_snelheid = int(input("Geef de max snelheid: > "))

print_boetes(filter_overtredingen(dict_metingen, max_snelheid))