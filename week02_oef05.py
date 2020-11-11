# Oef 05
# Vraag de decimale score (op 20) van een module aan de gebruiker. Print nadien af of hij/zij geslaagd is.
# Zorg ervoor dat de score correct afgerond wordt: indien het decimale gedeelte kleiner is dan 0,5 wordt
# er naar beneden afgerond. In het andere geval wordt er naar boven afgerond. Print ook de afgeronde
# score af.
# (Tip: maak gebruik van de ceil/floor-functionaliteit uit de module math)
import math

score = float(input("Geef uw score op: > "))

afgerond = math.ceil(score)
print(afgerond)
if afgerond < 10:
    
    print("helaas, volgende keer beter")
else:
    print("u bent geslaagd!")