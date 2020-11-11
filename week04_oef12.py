# Oef 12
# Schrijf een functie ‘zijn_totaal_verschillend’ die 2 lists binnenkrijgt.
# De functie geeft False terug indien er minimum één gemeenschappelijk element gevonden wordt.
# True wordt pas terug gegeven als beide helemaal verschillend zijn.

def zijn_totaal_verschillend(lijst1, lijst2):
    for element in lijst1:
        if element in lijst2:
            return False
    return True
            

list_getallen1 = [4, 5, 6, 4]
list_getallen2 = [89, 78, 4]

print(f"Controleer {list_getallen1} en {list_getallen2}: {zijn_totaal_verschillend(list_getallen1, list_getallen2)}")