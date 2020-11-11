# Oef 07
# Maak volgende lists aan:
# - een list met 4 gehele getallen
# - een list met 5 decimale getallen
# - een list met 3 strings
# Maak nu één functie ‘print_list’ die de verschillende elementen overloopt waarbij elk element samen met
# zijn index wordt afgeprint. Dit is een functie die enkel een (visueel)“deelprobleem” oplost én geen
# uitkomst returnt.

def print_list(lijst):
    for item in lijst:
        print(f"Getal {item} zit op positie {lijst.index(item)}")


verzameling1 = [12, 45, -9, -15]
verzameling2 = [12.23, 45.1, 9.478, 15.125, -3.14]
verzameling3 = ["Stijn", "Lies", "Henk"]

print_list(verzameling2)
