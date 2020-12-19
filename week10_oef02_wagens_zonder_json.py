# Oef 02
# Gegeven volgende beschrijving:
# Het taxibedrijf How@car heeft sinds kort, naast drie wagens ook twee lichte
# vrachtwagens rondrijden.
# Van elk voertuig wordt standaard het id, bouwjaar, het merk, het kmstand en de
# reisbestemming bijgehouden.
# Voor de personenwagens wordt er extra het maximum aantal passagierplaatsen en
# het aantal vervoerde personen bijgehouden.
# Analoog voor de lichte vrachtwagens wordt ook het maximaal toegelaten
# laadvermogen en het gewicht van de vervoerde vracht bijgehouden.
# Vanuit een monitorcentrum wenst men een applicatie die de status van alle
# personenwagens kan weergeven en aanpassen.
# Werkwijze - Dataklassen
# Maak de dataklasses Voertuig, Personenwagen en Vrachtwagen.
# Welke relatie bestaat er tussen deze klasses?
# Klasse Voertuig
# • Voorzie de klasse van de nodige private attributen:
# o id, merk, bouwjaar, kmstand, reisbestemming
# • Maak voor elk attribuut een publieke property aan.
# o id, merk en bouwjaar heeft enkel een getter property
# § Een merk wordt altijd in hoofdletters teruggegeven.
# o kmstand heeft een setter en getter property
# § Voorzie inputvalidatie in de property-setter.
# Een kmstand moet een geheel- of kommagetal zijn.
# o reisbestemming heeft een setter en getter property
# § Voorzie inputvalidatie in de property-setter.
# Een reisbestemming moet een string zijn.
# • (een lege string is ook geldig, let er dus op dat deze aanvaard
# wordt).
# • De constructor
# o heeft 4 parameters: id, merk, bouwjaar, kmstand
# Voertuig
# Personenwagen Vrachtwagen
# Week 10
# Basic Programming (skills) / 8
# o reisbestemming wordt ingesteld als lege string
# • Welke operators moet je overwriten om later volgende functionaliteiten te
# voorzien?
# o Voertuigen worden gesorteerd op het aantal afgelegde kilometers.
# o 2 voertuigen zijn gelijk aan elkaar als het id gelijk is.
# o Je moet zowel een object van het type Voertuig, als een list van een
# voertuigen kunnen afprinten.
# • Voorzie de klasse Voertuig van een static- attribuut ‘__aantal_voertuigen’
# (die het aantal gecreëerde objecten van deze klasse bijhoudt) en een staticmethode
# ‘geef_aantal_voertuigen’ die het aantal teruggeeft.
# Klasse Vrachtwagen erft van de klasse Voertuig
# • Voorzie de klasse van 2 extra attributen:
# o vracht, max_laadvermogen
# • Maak voor deze attributen een publieke propertie aan. Bij foutieve input geef
# je een ValueError terug
# o max_laadvermogen heeft een setter en getter property
# § Voorzie inputvalidatie in de property-setter.
# Het laadvermogen moet een geheel- of kommagetal zijn.
# o vracht heeft een setter en getter property
# § Voorzie inputvalidatie in de property-setter.
# Het gewicht van de vracht moet een geheel- of kommagetal zijn.
# Het gewicht van de vracht moet tevens kleiner zijn dat het
# laad vermogen
# • De constructor
# o heeft de 5 parameters: id, merk, bouwjaar, kmstand en
# max_laadvermogen
# o vracht wordt ingesteld op 0
# • Voorzie een gepaste ToString (str) methode.
# • Heeft een extra methode ‘geef_detail_info’
# o Zie het codevoorbeeld voor de gewenste output.
# Klasse Personenwagen erft van de klasse Voertuig
# • Voorzie de klasse van 2 extra attributen:
# o max_aantal_zitplaatsen, aantal_personen
# • Maak voor deze attributen een publieke propertie aan. Bij foutieve input geef
# je een ValueError terug
# o max_aantal_zitplaatsen heeft een setter en getter property
# § Voorzie inputvalidatie in de property-setter.
# Het max aantal zitplaatsen moet een geheel getal zijn én positief
# zijn
# o aantal_personen heeft een setter en getter property
# Week 10
# Basic Programming (skills) / 9
# § Voorzie inputvalidatie in de property-setter.
# Het aantal personen moet een geheel getal zijn én kan niet
# groter zijn dan het max_aantal_zitplaatsen.
# • Maak een extra getter-property (zonder attribuut) vrije_plaatsen
# o Deze property geeft het aantal vrije plaatsen weer in het voertuig. Hoe
# bereken je dit?
# • De constructor
# o heeft de 5 parameters: id, merk, bouwjaar, kmstand en
# max_aantal_zitplaatsen
# o aantal personen aan boord wordt ingesteld op 0
# • Voorzie een gepaste ToString methode.
# • Heeft een extra methode ‘geef_detail_info’
# o Zie het codevoorbeeld voor de gewenste output.
# Test uit door verschillende objecten van deze klasse aan te maken.
# De output kan er als volgt uitzien:

from modelweek10_2.Personenwagen import Personenwagen
from modelweek10_2.Vrachtwagen import Vrachtwagen

rental1 = Personenwagen(100, "Audi", 2010, 3000, 5)
rental2 = Personenwagen(101, "Volkswagen", 2016, 0, 5)
rental3 = Vrachtwagen(102, "DAF", 2009, 3000, 5000)

list_met_rentals = [rental1, rental2, rental3]
print("*** Dit zijn de beschikbare voertuigen ****")
for item in list_met_rentals:
    print(item)

print("*** Geef de nieuwe bestemming van de voertuigen ****")
for item in list_met_rentals:
    temp_reisbestemming = input(f"Voor {item} > ")
    item.reisbestemming = temp_reisbestemming

print("*** Er stappen 3 personen in de Volkswagen ****")
list_met_rentals[1].aantal_personen = 3
print("*** De vrachtwagen wordt geladen ****")
try:
    temp_vracht = float(input(
        f"Hoeveel vracht neemt deze vrachtwagen mee? (max: {list_met_rentals[2].max_laadvermogen}) > "))
    list_met_rentals[2].vracht = temp_vracht
except Exception as ex:
    print(f"Foutje: {ex}")

print("*** toon details per rental car ****")
for item in list_met_rentals:
    print(item.geef_detail_info())
