# Oef 11
# Schrijf een functie toon_max die 3 getallen binnenkrijgt. De functie geeft het maximum terug.

def toon_max(getal1, getal2, getal3):
    if getal1 > getal2 and getal1 > getal2:
        return getal1
    elif getal2 > getal1 and getal2 > getal3:
        return getal2
    elif getal3 > getal1 and getal3 > getal2:
        return getal3
    else:
        return "er waren getallen gelijk"

print(f"Het grootste getal is: {toon_max(5,6,3)}")