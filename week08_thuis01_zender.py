# • Stap 3 Maak een klasse Zender
# Van een Zender bewaar je in private attributen
# • de naam
# • de taal waarin ze uitzenden
# • en een list met programma’s die ze uitzenden.
# Maak de correcte publieke properties aan voor de attributen
# • De naam heeft een setter en getter property.
# • De taal heeft een setter en getter property.
# o Er kan enkel NL / ENG / FR worden bewaard in dit attribuut.
# o Wordt er toch een andere waarde doorgegeven, dan bewaar je “ERROR”.
# Bij het aanmaken van een instantie van de klasse Zender geef je 2 parameters mee in de
# constructor.
# • Naam en taal.
# • Het attribuut met programma’s wordt ingesteld als een lege lijst.
# Schrijf de __str__() methode.
# • De output zal er als volgt uitzien: "naam -> lijst met programma’s "
# Deze klasse bevat een extra methode voeg_programma_toe(programma)
# • Deze methode krijgt als parameter een instantie van de klasse programma mee.
# • Na controle of de parameter wel een programma is, voeg je deze toe aan de list met
# programma’s.
# Deze klasse bevat een extra methode zoek_afgelopen_programmas().
# • Deze methode heeft geen extra parameters
# • Deze methode geeft een lijst terug met alle programma’s die zijn afgelopen.
# Deze klasse bevat een extra methode selecteer_willekeurig_programma().
# • Deze methode heeft geen extra parameters
# • Deze methode geeft één willekeurig programma terug uit de lijst met programma’s.
# Hou, in de klasse zelf, tenslotte bij hoeveel keer er een instantie van deze klasse wordt
# aangemaakt.
# • Voorzie een static variabele en static methode geef_aantal_aangemaakte_zenders() om
# dit op te vragen.
# Week 08
# Basic Programming (skills) / 17
# Test dit tenslotte uit in de testklasse test_zenders.py.

from modelweek08.Presentator import Presentator
from modelweek08.Tvprogramma import Tvprogramma
from modelweek08.Zender import Zender


presentator1 = Presentator("Laura", "Tesoro")
presentator2 = Presentator("Nathalie", "Meskens")


programma1 = Tvprogramma("Belgium got talent", presentator1)
programma2 = Tvprogramma("Beste kijkers", presentator2)
programma2.is_actief = False

# Verkort
programma3 = Tvprogramma("The Late Late Show", Presentator("James", "Corden"))


zender1 = Zender("VTM", "NL")
zender2 = Zender("FOX", "ENG")
zender3 = Zender("TV China", "Chinees")

zender1.voeg_programma_toe(programma1)
zender1.voeg_programma_toe(programma2)
zender2.voeg_programma_toe(programma3)
zender2.voeg_programma_toe("dit zal niet lukken")

print("*** info zenders ***")
print(zender1)
print(zender2)
print(zender3)
print(f"**** volgende programma's zijn afgelopen van {zender1.naam}  ***")
print(zender1.zoek_afgelopen_programmas())
print(
    f"**** volgend programma wordt willekeurig gekozen van {zender1.naam} ***")
print(zender1.selecteer_willekeurig_programma())
print(
    f"Aantal verschillende zenders aangemaakt {Zender.geef_aantal_aangemaakte_zenders()}")
