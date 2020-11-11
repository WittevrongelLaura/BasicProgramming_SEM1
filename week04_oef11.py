# Oef 11
# Schrijf een functie ‘gemiddelde _in_list’ met als parameter een list van getallen die het gemiddelde van
# de getallen teruggeeft.
# getallen = [12, 45, 465, 78, 1, 23, 89]
# lege_lijst_getallen = []

def gemiddelde_in_list(list):
    gemiddelde = sum(list)/len(list)
    return gemiddelde

getallen = [12, 45, 465, 78, 1, 23, 89]
lege_lijst_getallen = []

print(f"Gemiddelde: {gemiddelde_in_list(getallen)}")