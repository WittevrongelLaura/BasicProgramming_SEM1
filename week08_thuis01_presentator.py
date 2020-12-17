# Thuis 1
# • Stap 1: Maak een klasse Presentator.
# Van een Presentator bewaar je in private attributen:
# • Naam
# • Voornaam
# Deze twee attributen hebben een getter en setter-property.
# Schrijf de constructor met 2 parameters (naam en voornaam)
# Schrijf de __str__() en __repr_() methode.
# • De output zal er als volgt uitzien: "presentator: naam, voornaam"
# Zorg ervoor dat je twee presentatoren met elkaar kan vergelijken, een presentator is gelijk aan een
# andere als én de naam én de voornaam gelijk zijn.
# Test deze klasse uit in een testklasse test_presentator.py

from modelweek08.Presentator import Presentator


presentator1 = Presentator("Laura", "Tesoro")
presentator2 = Presentator("Nathalie", "Meskens")
presentator3 = Presentator("Laura", "Omloop")
presentator_copy = Presentator("Laura", "Tesoro")

print("***test print***")
print(presentator1)
print("\n***test vergelijking***")
if presentator1 == presentator2:
    print(f"{presentator1} is gelijk aan {presentator2}")
else:
    print(f"{presentator1} is NIET gelijk aan {presentator2}")

if presentator1 == presentator3:
    print(f"{presentator1} is gelijk aan {presentator3}")
else:
    print(f"{presentator1} is NIET gelijk aan {presentator3}")


if presentator1 == presentator_copy:
    print(f"{presentator1} is gelijk aan {presentator_copy}")
else:
    print(f"{presentator1} is NIET gelijk aan {presentator_copy}")
