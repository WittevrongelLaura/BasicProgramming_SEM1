# Oef 01
# Zoek de klasse Bier uit labo week 7 op (of gebruik de klasse Bier uit het bronmateriaal).
# Pas deze klasse nu aan zodat
# • in elke resp. setter-property een controle op de nieuwe doorgegeven waarde
# gebeurt
# o biernaam, brouwerijnaam, kleur: nieuwe waarde is een string en mag
# niet leeg zijn;
# o alcoholpercentage: nieuwe waarde is een float en ligt tussen 0 en 100.
# • indien de nieuwe waarde niet voldoet, wordt een ValueError teruggegeven
# • een object van de klasse Bier (later in oef 2) in een list correct getoond wordt.
# Test uit door:
# • maak een correct bier-object aan. Wijzig nadien de naam van het bier in een
# lege string.
# • maak een bier aan waarbij je voor de brouwerij een lege string doorgeeft.

from modelweek09.Bier import Bier


def test1():
    #bier = Bier("NMCT-Blond", "Howest",  "blond", 25.0)#kleur en alcoholpercentage omgekeerd
    try:
        bier = Bier("NMCT-Blond", "Howest", 25.0, "blond")
        print(bier)
        # geef een blanco naam op, via de input
        nieuwe_naam = input("Geef een nieuwe biernaam op:> ")
        bier.naam = nieuwe_naam
        print(bier)
    except ValueError as ex:
        print(f"Foutmelding: {ex}")#foutieve biernaam komt van valueError in bier.py


#test1()

def test2():
    try:
        biernaam = input("Geef de biernaam op:> ")
        brouwerijnaam = input("Geef de brouwerij op:> ")
        kleur = input("Geef de kleur op:> ")
        alcoholpercentage = float(input("Geef het alcoholpercentage op:> "))
        print("Bier aanmaken...")
        bier = Bier(biernaam, brouwerijnaam, alcoholpercentage, kleur)
        print(bier)
    except ValueError as ex:
        print(f"Foutmelding: {ex}")
    except Exception:
        print(f"Er is nog een andere soort fout opgetreden")

test2()
