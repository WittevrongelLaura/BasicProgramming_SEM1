# Oef 04
# Maak nu één functie ‘print_dictionary’ die de verschillende elementen overloopt waarbij
# telkens key & value samen op één lijn worden afgeprint. De functie heeft als parameters een
# naam (voor de dictionary) en de dictionary zelf. Voorbeeld:
# Dictionary MCT:
# key: 1MCT -> value: 101
# key: 2MCT -> value: 88
# key: 3MCT -> value: 77
# Dictionary MIT:
# key: 1MIT -> value: 58
# key: 2MIT -> value: 36
# Dictionary Devine:
# key: 1Devine -> value: 123
# key: 2Devine -> value: 98
# key: 3Devine -> value: 55

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"key: {key} -> value: {value}")

MCT = {"1MCT": 131, "2MCT": 88, "3MCT": 77}
MIT = {"1MIT": 58, "2MIT": 36}
Devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

print_dictionary(MCT)
print_dictionary(MIT)
print_dictionary(Devine)