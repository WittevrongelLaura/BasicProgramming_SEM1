# Oef 09
# Schrijf een functie ‘max_en_min_uit_list’ met als parameter een list. Deze functie zoekt uit de list het
# maximum en minimum op en geeft deze samen in een string terug. Test deze functie uit op een list met
# getallen en een list met woorden.
# Uit [11, 52, 125, -89, 1245] is het max: 1245 en min: -89
# Uit ['jan', 'feb', 'maa', 'apr', 'mei'] is het max: mei en min: apr

def max_en_min_uit_list(lijst):
    kleinste_getal = min(lijst)
    grootste_getal = max(lijst)
    return kleinste_getal, grootste_getal

lijst_getallen = [11, 52, 125, -89, 1245]
lijst_woorden = ["jan", "feb", "maa", "apr", "mei"]

print(max_en_min_uit_list(lijst_getallen))
print(max_en_min_uit_list(lijst_woorden))