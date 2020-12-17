# Thuis 2
# Maak een dataklasse Breuk aan waarbij we de teller en noemer gaan bijhouden. Volg
# opnieuw volgend stappenplan.
# Basis:
# • Programmeer de methode __init__()
# o De parameters zijn teller en noemer
# • Voorzie voor elk vermeld attribuut een property-methode.
# • Programmeer de methode __str__()
# Uitbreiding:
# • Voorzie een public methode vereenvoudig(): hierbij wordt gekeken of teller en
# noemer door berekening van de grootste gemene deler kunnen vereenvoudigd
# worden
# o Python voorziet een functie om de grootst gemene deler te bepalen.
# https://docs.python.org/3.8/library/math.html#math.gcd
# • (na de theorie van week 8) Programmeer de methode __add__(…) die toelaat om
# twee breuken te laten optellen via de +-operator. Werk zelf de andere methodes
# uit: verschil, product en deling.
# Test voldoende uit door verschillende objecten van deze klasse aan te maken. Test
# vervolgens de methode ‘vereenvoudig’, de bewerkingen tussen breuken onderling.
# Je kan hiervoor het testbestand op Leho gebruiken.

# test class Breuk
from modelweek07.Breuk import Breuk

print("Breuk 1: ")
b1 = Breuk(3, 4)
print(b1)
print("Noemer wijzigen naar 6: ")
b1.noemer = 6
print(b1)
print("Breuk 1  laten vereenvoudigen: ")
b1.vereenvoudig()
print(b1)

print("\nBreuk 2 na vereenvoudiging: ")
b2 = Breuk(4, 10)
b2.vereenvoudig()
print(b2)
#print("Som van Breuk 1 en Breuk 2: ")
#som = b1 + b2
#print(som)
