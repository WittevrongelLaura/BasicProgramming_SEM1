# Oef 05
# Maak een nieuwe lege dictionary ‘Howest’ aan. Voeg bovenstaande dictionaries eraan toe.



MCT = {"1MCT": 131, "2MCT": 88, "3MCT": 77}
MIT = {"1MIT": 58, "2MIT": 36}
Devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

howest = {}
howest.update(MCT)
howest.update(MIT)
howest.update(Devine)

print(howest)