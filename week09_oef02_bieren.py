# Oef 02
# Voor de volgende oefeningen kan je je baseren op de besproken demo uit de theorieles.
# Download het bronbestand ‘bieren.json’. Bestudeer grondig het bestand.
# Zoals je in de theorieles besproken hebt, zal de opbouw van een json bestand steeds
# verschillen. De ene keer bestaat het uit een list[], de andere keer uit een dictionary{}.
# De doelstelling van deze oefening is om voor elk beschreven bier uit het bestand een
# object van de klasse Bier aan te maken. Alle gecreëerde objecten houden we in een list
# bij. Nadien voegen we een extra filterfunctionaliteit toe: het filteren van bieren op
# basis van een opgegeven brouwerijnaam.
# Werkwijze:
# 1: Plaast dit bestand in een afzonderlijke submap ‘doc’.
# 2: Voeg een nieuw bestand BierRepository.py in de map ‘model’ toe. Maak hierin een
# nieuwe klasse BierRepository aan.
# 3: Programmeer volgende onderdelen:
# • Voorzie de klasse van een private klasse-attributte “__filename” die het pad
# naar het bronbestand bijhoudt. Bijvoorbeeld:
# __filename = "doc/bieren.json"
# • Voeg een public static methode ‘inlezen_bieren’ toe die in staat is om het
# bronbestand in te lezen en een list van bieren terug te geven.
# o Om een lokaal json-file in te lezen maakt de public static methode
# ‘inlezen_bieren’ gebruik van volgende private static hulpmethode
# ‘__inlezen_local_json_file’.
# o importeer bovenaan de json-library zodat je een json file eenvoudig kan
# bevragen:
# import json

# De methode __inlezen_local_json_file geeft in deze situatie een list [] terug
# waarvan elk element op zijn beurt een een dictonary {} is.
# Overloop in de methode inlezen_bieren binnen de for-lus elk element uit deze
# list.
# Elk element wordt voorgesteld als een dictionary met bijhorende key en value.

# Vraag met de juiste key (let op voor hoofdletter gebruik in de json file!) elke
# waarde op. Maak met alle info een object van de klasse Bier.
# • Opgelet: niet elke vermelde waarde is correct. Gebruik daarom exception handling
# bij het inlezen.
# Test de methode voldoende uit:

# Zorg dat de ingelezen list van bier-objecten op basis van het alcoholpercentage
# van klein naar groot kan gesorteerd worden.
# o Welke operator moet je hiervoor overloaden? In welke klasse?
# Voeg een static methode ‘zoek_bier_uit_brouwerij’ toe met parameters een
# list van objecten van de klasse Bier én een brouwerijnaam. Doorloop alle bieren
# en geef enkel deze bieren terug afkomstig uit de doorgegeven brouwerij.

from modelweek09.Bier import Bier
from modelweek09.BierRepository import BierRepository


def print_bieren(lijst_bieren):
    for bier in lijst_bieren:
        print(f"{bier} -> alcoholpercentage: {bier.alcoholpercentage}")


def test_bieren_a():
    # opgave a
    lijst_bieren = BierRepository.inlezen_bieren()
    print(f"Aantal correct ingelezen bieren zijn: {len(lijst_bieren)}")
    print(f"Inhoud van de lijst met bieren: {lijst_bieren}")


# test_bieren_a()


def test_bieren_b():
    # opgave b
    lijst_bieren = BierRepository.inlezen_bieren()
    lijst_bieren.sort()
    print_bieren(lijst_bieren)


# test_bieren_b()


def test_bieren_c():
    # opgave c
    lijst_bieren = BierRepository.inlezen_bieren()
    lijst_bieren.sort()
    deel_brouwerij = input("\nGeef (een deel van) de brouwerijnaam op: ")
    print("Gevonden bieren zijn: ")
    resultaat = BierRepository.zoek_bieren_uit_brouwerij(
        lijst_bieren, deel_brouwerij)
    print_bieren(resultaat)

test_bieren_c()
