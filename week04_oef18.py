# Oef 18
# Van deze oefening zijn er twee versies. Een niveau C oefening, die verdergaat in een niveau D oefening.
# In een bedrijf werken arbeiders, bedienden en kaderpersoneel.
# Schrijf een programma die voor diverse werknemers, op basis van hun functie (arbeider, bediende of
# kader), het totale brutoloon berekent van de werknemersgroep binnen dezelfde functie.
# Maw. per werknemer wordt de functie (A, B of K) en het brutoloon ingevoerd. Hou de ingevoerde
# gegevens in lists bij.
# Let wel:
# Als alle werknemers werden ingevoerd moeten volgende zaken worden getoond:
# • het aantal arbeiders,
# • het aantal bedienden,
# • het aantal kaderleden,
# • het totaal aantal werknemers,
# • het totaal brutoloonbedrag.
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
# A 1800€
# A 1560€
# B 2000€
# B 2400€
# K 3500€
# Aantal werknemers: 5
# Aantal arbeiders: 2
# Aantal bedienden: 2
# Aantal kaderpersoneel: 1
# Totaal brutoloon: 11260€

def print_loon_van_list(lijst_met_lonen, type_werknemer):
    for element in lijst_met_lonen:
        print(f"{type_werknemer} \t {element}€")

brutowedde_arbeider = []
brutowedde_bediende = []
brutowedde_kader = []


# brutowedde_na_inlevering_arbeider = []
# brutowedde_na_inlevering_bediende = []
# brutowedde_na_inlevering_kader = []

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

print("Overzicht:\n")
print_loon_van_list(brutowedde_arbeider, "A")
print_loon_van_list(brutowedde_bediende, "B")
print_loon_van_list(brutowedde_kader, "K")

alle_lijsten_samen = brutowedde_arbeider + brutowedde_bediende + brutowedde_kader
print(f"Aantal werknemers: {len(alle_lijsten_samen)}")
print(f"Aantal arbeiders: {len(brutowedde_arbeider)}")
print(f"Aantal bedienden: {len(brutowedde_bediende)}")
print(f"Aantal kader: {len(brutowedde_kader)}")

print(f"Totaal brutoloon: {sum(alle_lijsten_samen)}€")