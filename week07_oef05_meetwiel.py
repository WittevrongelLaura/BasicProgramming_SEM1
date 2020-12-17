# Oef 05
# We wensen van elk wiel de straal en het aantal omwentelingen bij te houden. Hiervoor
# maken we een klasse Meetwiel met de attributen straal en omwentelingen.
# Volgend stappenplan kan gevolgd worden:
# • Voorzie de klasse van de nodige (private) attributen
# • Voorzie de bijhorende getter en setter property-methodes.
# • Voorzie ook 2 extra getter property-methodes:
# o Deze twee properties hebben geen bijhorde attributen (opslagplaats), dit
# komt omdat ze gebruik maken van de andere attributen om “iets” te
# berekenen. Hierdoor hebben ze ook geen setter propertie.
# § Programmeer de getter property-methode omtrek:
# deze geeft de omtrek van het wiel terug
# § Programmeer de getter property-methode afstand:
# deze geeft de afgelegde afstand ifv de het aantal omwentelingen en
# de omtrek van het meetwiel terug
# • Programmeer de constructor: methode __init__()
# o Heeft de volgende optionele parameters straal en omwentelingen
# (default-waarde voor deze 2 parameters is 0).
# • Programmeer de methode __str__()
# o Geeft volgende output:
# Meetwiel met straal straal en omwentelingen omwentelingen.
# Test voldoende uit door verschillende objecten van deze klasse aan te maken. Je kan
# hiervoor ook het testbestand op Leho gebruiken.
# Vraag tenslotte aan de gebruiker meerdere extra omwentelingen voor een wiel op.
# Sluit af met ‘c’. Print nadien de afgelegde afstand opnieuw af. Voorbeeld:
# from model.Meetwiel import Meetwiel
# meetwiel1 = Meetwiel(0.9) # straal
# meetwiel2 = Meetwiel(0.45, 123) # straal , omwentelingen
# print(meetwiel1)
# print(meetwiel2)
# waarde = input(
# "Geef het aantal extra omwentelingen door of sluit af met 'c':> ")
# while (waarde != "c" and waarde.isnumeric()):
# meetwiel1.omwentelingen += int(waarde)
# waarde = input(
# "Geef het aantal extra omwentelingen door of sluit af met 'c':> ")
# print(meetwiel1)
# print(f"Meetwiel 1 legde reeds {meetwiel1.afgelegde_afstand:.2f} m af")
# Terminal
# Meetwiel met straal 0.9 en omwentelingen 0
# Meetwiel met straal 0.45 en omwentelingen 123
# Geef het aantal extra omwentelingen door of sluit af met 'c':> 2
# Geef het aantal extra omwentelingen door of sluit af met 'c':> 1
# Week 07
# Basic Programming (skills) / 10
# Geef het aantal extra omwentelingen door of sluit af met 'c':> 3
# Geef het aantal extra omwentelingen door of sluit af met 'c':> c
# Meetwiel met straal 0.9 en omwentelingen 6
# Meetwiel 1 legde reeds 33.93 m af

# Test class Meetwiel
from modelweek07.Meetwiel import Meetwiel

meetwiel1 = Meetwiel(0.9)  # straal
meetwiel2 = Meetwiel(0.45, 123)  # straal , omwentelingen
print(meetwiel1)
print(meetwiel2)

waarde = input(
    "Geef het aantal extra omwentelingen door of sluit af met 'c':> ")
while (waarde != "c" and waarde.isnumeric()):
    meetwiel1.omwentelingen += int(waarde)
    waarde = input(
        "Geef het aantal extra omwentelingen door of sluit af met 'c':> ")
print(meetwiel1)
print(f"Meetwiel 1 legde reeds {meetwiel1.afstand:.2f} m af")
