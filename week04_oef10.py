# Oef 10
# Schrijf een functie ‘som_in_list’ met als parameter een list van getallen die de totale som van de list
# getallen teruggeeft.
# - Pas eerst de techniek van vorige week toe.
# - Zoek nadien of er geen ingebouwde functie bestaat om de som te berekenen van de inhoud van
# een list.

def som_in_list(lijst):
    return sum(lijst)

lijst_getallen = [5, 6, 9, 5 , 6]
print(f"De som is {som_in_list(lijst_getallen)}")

