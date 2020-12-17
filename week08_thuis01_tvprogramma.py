# • Stap 2: Maak een klasse Tvprogramma
# Van een Tv programma bewaar je in private attributen
# • de titel
# • presentator
# • is_actief (of het al dan niet wordt uitgezonden)
# Maak de publieke properties aan voor deze attributen
# • De titel heeft enkel een getter property
# • De presentator heeft een setter en getter property.
# o De setter property aanvaardt enkel een value die van het type Presentator is.
# Wordt een andere waarde doorgegeven, dan bewaar je de string “ERROR”
# • is_actief heeft een setter en getter property.
# o De setter property aanvaardt enkel een value True of False.
# (Op welk type zal je controleren)
# o Wordt er een andere waarde doorgegeven, dan bewaar je False.
# Schrijf de constructor die 2 parameters binnenkrijgt.
# • De titel en presentator.
# • De constructor stelt echter wel alle 3 de attributen in. Het attribuut is_actief krijgt de
# waarde True bij het aanmaken van een instantie.
# Schrijf tenslotte nog een __str__() en __repr__() methode.
# • Deze twee methodes geven volgende (zelfde) output.
# o TV Programma: titel door <<presentator>>
# Test de klasse associatie tussen Presentator en Tvprogramma uit in een testklasse
# test_tvprogramma.py

from modelweek08.Presentator import Presentator
from modelweek08.Tvprogramma import Tvprogramma


presentator1 = Presentator("Laura", "Tesoro")
presentator2 = Presentator("Nathalie", "Meskens")
programma1 = Tvprogramma("Belgium got talent", presentator1)
programma2 = Tvprogramma("Beste kijkers", presentator2)
programma2.is_actief = False

# Verkort
programma3 = Tvprogramma("The Late Late Show", Presentator("James", "Corden"))

# geeft een fout
programma4 = Tvprogramma("The Simpsons", "Homer Simpson")
print("*** toon info ***")
print(programma2)
print(programma3)
print(programma4)
print(f"{programma2} is momenteel actief: {programma2.is_actief}")
programma2.is_actief = True
print(f"{programma2} is momenteel actief: {programma2.is_actief}")
programma2.is_actief = "blablablabla"
print(f"{programma2} is momenteel actief: {programma2.is_actief}")
