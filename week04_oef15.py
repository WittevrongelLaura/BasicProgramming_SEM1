# Oef 15
# Schrijf een functie ‘verwijder_dubbels’ die een list als parameter heeft. Deze functie geeft een nieuwe list
# zonder duplicaten terug. Test uit door de beide lists af te printen.
# ['A', 89, 78, 4, 'A', 'test', 4]
# Zonder dubbels: ['A', 89, 78, 4, 'test']

def verwijder_dubbels(lijst):
    nieuwe_list = []
    for item in lijst:
        if not item in nieuwe_list:
            nieuwe_list.append(item)
    return nieuwe_list

test = ["A", 89, 78, 4, "A", "test", 4]
print(f"{test}\nZonder dubbels: {verwijder_dubbels(test)}")