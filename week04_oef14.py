# Oef 14
# Schrijf een functie ‘geef_gemeenschappelijke_elementen’ die 2 lists binnenkrijgt.
# De functie bepaalt de gemeenschappelijke elementen en geeft deze als een nieuwe list terug. Zorg ervoor
# dat er in de laatste list geen dubbels voorkomen. Zorg ook dat deze gesorteerd is. Print vervolgens alles
# af.
# Test uit op twee lists van getallen en op twee lists van woorden.
# List1: [78, 4, 5, 6, 4]
# List2: [89, 78, 4]
# Doorsnede: [4, 78]
# List1: ['Tamara', 'Delfien', 'Elke', 'Marijn']
# List2: ['Natasja', 'Mieke', 'Tamara', 'Elke', 'Carine']
# Doorsnede: ['Elke', 'Tamara']


def geef_gemeenschappelijke_elementen(lijst1, lijst2):
    nieuwe_list=[]
    for element in lijst1:
        if element in lijst2 and not element in nieuwe_list:
            nieuwe_list.append(element)
    nieuwe_list.sort()
    return nieuwe_list


list_getallen1 = [78, 4, 5, 6, 4]
list_getallen2 = [89, 78, 4]
print(f"List1: {list_getallen1} ")
print(f"List2: {list_getallen2} ")
print(f"De doorsnede is {geef_gemeenschappelijke_elementen(list_getallen1, list_getallen2)}")