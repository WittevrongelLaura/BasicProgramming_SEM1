# Oef 18
# De vorige oefening wordt complexer en gaat verder tot een niveau D oefening.
# In een bedrijf werken arbeiders, bedienden en kaderpersoneel. Om hun firma van het faillissement te
# redden leveren arbeiders, bedienden en kaderpersoneel een percentage van hun brutoloon in. Voor
# arbeiders is dat 5 % van het brutoloon, voor bedienden is dat 8 % en het kaderpersoneel levert 10 % in.
# Schrijf een programma die voor diverse werknemers, op basis van hun functie (arbeider, bediende of
# kader) en hun brutoloon, berekent hoeveel het in te leveren bedrag bedraagt. Maw. per werknemer wordt
# de functie (A, B of K) en het brutoloon ingevoerd. Hou de ingevoerde gegevens in lists bij.
# Week 04
# Basic Programming (skills) / 8
# Let wel:
# Als alle werknemers werden ingevoerd moeten volgende zaken worden getoond:
# • het aantal arbeiders,
# • het aantal bedienden,
# • het aantal kaderleden,
# • het totaal aantal werknemers,
# • het totaal brutoloonbedrag (voor afhouden van het in te leveren bedrag),
# • het totaal brutoloonbedrag (na afhouden van het in te leveren bedrag).
# • De totale besparing voor het bedrijf
# Geef het aantal werknemers op:> 5
# Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > B
# Geef het brutowedde op:> 2000
# Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > A
# Geef het brutowedde op:> 1800
# Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > A
# Geef het brutowedde op:> 1560
# Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > K
# Geef het brutowedde op:> 3500
# Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > B
# Geef het brutowedde op:> 2400
# Overzicht:
# A 1800€ -> 1710.0€
# A 1560€ -> 1482.0€
# B 2000€ -> 1840.0€
# B 2400€ -> 2208.0€
# K 3500€ -> 3150.0€
# Aantal werknemers: 5
# Aantal arbeiders: 2
# Aantal bedienden: 2
# Aantal kaderpersoneel: 1
# Totaal brutoloon: 11260€
# Totaal brutoloon na de inlevering: 10390.0€
# Totale inlevering: 870.0€

def print_loon_van_list(lijst_met_lonen, type_werknemer):
    for element in lijst_met_lonen:
        print(f"{type_werknemer} \t {element}€")

#overloop de 2 lijsten op hetzelfde tempo
#beide lijsten zijn even lang
#neem steeds het element op de volgende index
def print_loon_van_list_met_inleveren(lijst_met_lonen, lijst_met_lonen_na_inleveren, type_werknemer):
    for index in range(0, len(lijst_met_lonen)):
        element_loon = lijst_met_lonen[index]
        element_loon_na_inleveren = lijst_met_lonen_na_inleveren[index]
        print(f"{type_werknemer} \t {element_loon} ---> {element_loon_na_inleveren}")

def lever_in(lijst_met_lonen, inleverpercentage):
    resultaat_lijst = []
    for loon in lijst_met_lonen:
        loon_na_inleveren = loon - loon * inleverpercentage
        resultaat_lijst.append(loon_na_inleveren)
    return resultaat_lijst

brutowedde_arbeider = []
brutowedde_bediende = []
brutowedde_kader = []

aantal_werknemers = int(input("Met hoeveel man werk je daar? > "))
for index in range(0,aantal_werknemers):
    functie = input("Geef de functie op (A: Arbeider, B: Bediende, K: Kaderpersoneel): > ")
    huidig_loon = int(input("Geef brutoloon > "))
    if functie.lower() == "a":
        brutowedde_arbeider.append(huidig_loon)
    elif functie.lower() == "b":
        brutowedde_bediende.append(huidig_loon)
    elif functie.lower() == "k":
        brutowedde_kader.append(huidig_loon)
    else:
        print("leer typen")

brutowedde_na_inlevering_arbeider = lever_in(brutowedde_arbeider, 0.05)
brutowedde_na_inlevering_bediende = lever_in(brutowedde_bediende, 0.08)
brutowedde_na_inlevering_kader = lever_in(brutowedde_kader, 0.10)

print("Overzicht:\n")
# print_loon_van_list(brutowedde_arbeider, "A")
# print_loon_van_list(brutowedde_bediende, "B")
# print_loon_van_list(brutowedde_kader, "K")
print_loon_van_list_met_inleveren(brutowedde_arbeider, brutowedde_na_inlevering_arbeider, "A")
print_loon_van_list_met_inleveren(brutowedde_bediende, brutowedde_na_inlevering_bediende, "B")
print_loon_van_list_met_inleveren(brutowedde_kader, brutowedde_na_inlevering_kader, "K")

alle_lijsten_samen = brutowedde_arbeider + brutowedde_bediende + brutowedde_kader
print(f"Aantal werknemers: {len(alle_lijsten_samen)}")
print(f"Aantal arbeiders: {len(brutowedde_arbeider)}")
print(f"Aantal bedienden: {len(brutowedde_bediende)}")
print(f"Aantal kader: {len(brutowedde_kader)}")

print(f"Totaal brutoloon: {sum(alle_lijsten_samen)}€")
print(f"Totaal brutoloon na inlevering: {sum(brutowedde_na_inlevering_arbeider + brutowedde_na_inlevering_bediende + brutowedde_na_inlevering_kader)}€")