# Oef 09
# Laat je applicatie een getal kiezen tussen 1 en 20. Laat vervolgens de gebruiker naar het getal raden. Bij
# iedere poging krijgt hij feedback: “kleiner” of “groter”. De applicatie stopt pas als het getal geraden is.
# Je toont hoeveel maal de gebruiker gokte.
# Tip: maak uit de module ‘random’ gebruik van de functionaliteit ‘random’:
# https://docs.python.org/3/library/random.html

import random

te_raden_getal = random.randint(1,20)

ingave = int(input("Doe een gokje tussen 1 en 20: > "))
aantal_gokken = 1

while ingave != te_raden_getal:
    if ingave > te_raden_getal:
        print("lager")
    else:
        print("hoger")
    aantal_gokken += 1
    ingave = int(input("Doe een opnieuw een gokje: > "))

print(f"Proficiat. Gevonden!\n\tU Gokte: {aantal_gokken} maal")