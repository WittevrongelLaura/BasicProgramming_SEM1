# Oef 02
# Maak één functie ‘print_tuple’ die de verschillende elementen overloopt waarbij elk element
# samen met zijn index wordt afgeprint. De functie heeft als parameters een naam (voor de
# tuple) en de tuple zelf.
# Voorbeeld:
# Verzameling MCT:
# 1MCT zit op positie 0
# 2MCT zit op positie 1
# 3MCT zit op positie 2
# Verzameling Devine:
# 1Devine zit op positie 0
# 2Devine zit op positie 1
# 3Devine zit op positie 2

def print_tuple(tuple):
    for element in tuple:
        print(f"{element} zit op positie {tuple.index(element)}")

tuple1 = ("1MCT", "2MCT", "3MCT")

print_tuple(tuple1)