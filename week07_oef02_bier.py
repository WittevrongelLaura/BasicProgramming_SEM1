# Oef 02
# Bestudeer het bronbestand bieren.csv.
# Door welke zaken wordt een bier gekenmerkt? Maak nu een dataklasse Bier.
# • Voorzie de klasse van de nodige (private) attributen: naam, brouwerij,
# alcoholpercentage, kleur
# • Maak voor elk attribuut een (publieke) property aan.
# o In de setter property voor naam, brouwerij en kleur
# § Wordt de nieuwe waarde gecontroleerd: een lege string wordt als
# ‘onbekend’ bewaard.
# o In de setter property voor alcoholpercentage controleer je of
# § Het een float is.
# § Het tussen 0 en 100 ligt.
# § Zoniet bewaar je de waarde -1 in zijn private attribuut.
# o De getter property voor naam wordt altijd in hoofdletters weergegeven.
# • Programmeer de constructor: de methode __init__()
# o De parameters zijn de vier attributen.
# • Programmeer de methode __str__()
# o De output is “naam brouwerij - alcoholpercentage”
# Maak verschillende bieren aan. Wijzig nadien de attributen via de setter-property.
# Controleer of de functionaliteit in orde is. Je kan hiervoor ook het testbestand op Leho
# gebruiken.
# # Test class test_bier.py
# from model.Bier import Bier
# print("** Bier 1 ***")
# b1 = Bier("Augustijn", "Bios", 12.0, "amber")
# print(b1)
# # verander de brouwerij naar lege string
# b1.brouwerij = ""
# print(b1)
# Terminal
# ** Bier 1 ***
# AUGUSTIJN Bios - 12.0
# AUGUSTIJN onbekend - 12.0
# Week 07
# Basic Programming (skills) / 6
# # Test class test_bier.py
# from model.Bier import Bier
# print("** Bier 2 ***")
# b2 = Bier("Jupiler", "", 3.3, "blond")
# print(f"Het kleur van {b2.naam} is {b2.kleur} ")
# print(f"Alcoholpercentage: {b2.alcoholpercentage} ")
# b2.alcoholpercentage = "5,5"
# print(f"Alcoholpercentage: {b2.alcoholpercentage} ")
# Terminal
# ** Bier 2 ***
# Het kleur van JUPILER is blond
# Alcoholpercentage: 3.3
# Alcoholpercentage: -1


# Test class Bier
from modelweek07.Bier import Bier

print("** Bier 1 ***")
b1 = Bier("Augustijn", "Bios", 12.0, "amber")
print(b1)


# verander de brouwerij naar lege string
# b1.brouwerij = ""
# print(b1)

print("** Bier 2 ***")
b2 = Bier("Jupiler", "", 3.3, "blond")
print(f"Het kleur van {b2.naam} is {b2.kleur} ")
print(f"Alcoholpercentage: {b2.alcoholpercentage} ")
# verander het percentage naar een ongeldige waarde
b2.alcoholpercentage = "5,5"
print(f"Alcoholpercentage: {b2.alcoholpercentage} ")
