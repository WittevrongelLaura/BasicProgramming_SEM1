# Oef 04
# Gegeven het bronbestand spelers.txt. Dit bronbestand staat in de submap ‘doc’ in. Analyseer
# het bronbestand: elke regel bestaat uit de gegevens van een voetbalspeler. Maak een
# applicatie die het bronbestand inleest, en vervolgens 11 verschillende spelers willekeurig
# selecteert om als ploegopstelling te kunnen fungeren. Deze 11 spelers worden in een nieuw
# bestand weggeschreven.
# Bepaal vooraf welke datastructuur je zal gebruiken om alle data bij te houden.
# Werk vervolgens in deelproblemen door oa. gebruik te maken van onderstaande functies:
# - Functie ‘inlezen_spelers’ die het bronbestand correct inleest en de data in een
# datastructuur teruggeeft
# - Functie ‘print_spelers’ die in staat is om alle spelers uit de gekozen datastructuur af te
# printen
# - Functie ‘selecteer_random_elftal’ die in staat is om 11 verschillende spelers willekeurig te
# selecteren en terug te geven.
# - Functie ‘opslaan_ploegopstelling’ die in staat is om een opstelling naar een tekstbestand
# weg te schrijven.
# Test voldoende uit.

import random
# ENKEL MCT!
# Gebruik bestand in doc/spelers.txt

# -	Functie ‘inlezen_spelers’ die het bronbestand correct inleest en de data in een datastructuur teruggeeft
# -	Functie ‘print_spelers’ die in staat is om alle spelers uit de gekozen datastructuur af te printen
# -	Functie ‘selecteer_random_elftal’ die in staat is om 11 verschillende spelers willekeurig te selecteren en terug te geven.
# -	Functie ‘opslaan_ploegopstelling’ die in staat is om een opstelling naar een tekstbestand  weg te schrijven.


def inlezen_spelers(bestandsnaam):
    list_alle_spelers = []
    fo = open(bestandsnaam)
    lijn = fo.readline().rstrip("\n")

    while lijn != "":
        # verwerken van 1 lijn
        list_alle_spelers.append(lijn)
        # volgende lijn nog eens lezen anders stopt hij niet
        lijn = fo.readline().rstrip("\n")
    fo.close()
    return list_alle_spelers


def print_spelers(een_list_met_spelers):
    x = 1
    for speler in een_list_met_spelers:
        print(f"{x}: {speler}")
        x += 1


def selecteer_random_elftal(een_lijst_met_spelers):
    list_met_geselecteerde_spelers = []
    while len(list_met_geselecteerde_spelers) < 11:
        # random
        # speler_index = random.randint(0, len(een_lijst_met_spelers)-1)
        # speler = een_lijst_met_spelers[speler_index]
        speler = random.choice(een_lijst_met_spelers)
        if not speler in list_met_geselecteerde_spelers:
            # anders dezelfde mensen
            list_met_geselecteerde_spelers.append(speler)
        # tot ik random 11 verschillende spelers heb, iets tovoegen
        # aan een list
    return list_met_geselecteerde_spelers


def opslaan_ploegopstelling(een_list_met_personen, bestandsnaam):
    fo = open(bestandsnaam, 'w')
    for speler in een_list_met_personen:
        fo.write(f"{speler}\n")
    fo.close()

list_mijn_ploeg = inlezen_spelers("docweek06/spelers.txt")
print(list_mijn_ploeg)

print_spelers(list_mijn_ploeg)

list_selectie = selecteer_random_elftal(list_mijn_ploeg)
print("**** SELECTIE *****")
print_spelers(list_selectie)

opslaan_ploegopstelling(list_selectie, "docweek06/speeldag8.txt")
print("*** BESTAND AANGEMAAKT")