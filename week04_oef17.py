# Oef 17
# Schrijf een functie ‘kies_5_getallen’ die twee waarden (min en max) als parameter binnenkrijgt. De
# functie kiest 5 unieke getallen uit het interval [min,max], voegt deze toe aan een list en geeft uiteindelijk
# deze list terug.
# Opgelet: er mogen geen dubbels in de teruggegeven lijst voorkomen.
# Test voldoende uit.
# Geef het minimum op:> 12
# Geef het maximum op:> 86
# De vijf geselecteerde getallen hiertussen zijn: [12, 17, 13, 14, 18]
import random

def kies_5_getallen(min, max):
    nieuwe_lijst = []
    while len(nieuwe_lijst) < 5:
        rand_getal = random.randint(min, max)
        if not rand_getal in nieuwe_lijst:
            nieuwe_lijst.append(rand_getal)
    return nieuwe_lijst

#getal1 = int(input("Geef het minimum op:> "))
#getal2 = int(input("Geef het maximum op:> "))


print(f"De vijf geselecteerde getallen hiertussen zijn: {kies_5_getallen(10, 20)}")