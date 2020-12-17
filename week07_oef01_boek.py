# Oef 01
# Maak een dataklasse Boek. Wat zijn de kenmerken waarmee een boek zich kan
# identificeren? Codeer nu deze dataklasse:
# • Maak in je folder 2020-2021-basicprog-week07 een folder “model” aan, in deze
# folder creeër je de file Boek.py
# • In de folder 2020-2021-basicprog-week07 maak je een file test_boek.py
# • Voorzie de klasse Boek van de nodige private attributen
# o titel, auteur, uitgeverij, isbn, jaargang
# • Maak voor elk attribuut een publiek getter en setter property-methode aan.
# • Programmeer de constructor: de methode __init__().
# o Deze heeft 5 parameters: titel, auteur, uitgeverij, isbn, jaargang
# o Zoals je kan afleiden uit de testcode, is de vijfde parameter optioneel.
# Wordt de jaargang niet opgegeven in de constructor dan krijgt het de
# default waarde 2020.
# • Programmeer de methode __str__()
# o De gewenste output van deze methode is “auteur, titel (uitgeverij)
# *jaargang*”
# Test uit door verschillende objecten van deze klasse aan te maken. Gebruik hiervoor
# een afzonderlijk bestand test_boek.py. Je kan hiervoor ook het testbestand op Leho
# gebruiken.
# # Test class test_boek.py
# from model.Boek import Boek
# b1 = Boek("Python for dummies", "Louis Kegels", "Arco", "125-875-5455")
# print(f"Titel van boek 1: {b1.titel}")
# b1.titel = "Python for dummies bis"
# print("Volledige info boek 1")
# print(b1)
# b2 = Boek("Hoe leg ik een vijver in mijn tuin aan? Deel 1",
# "Johan Vannieuwenhuyse", "Aveve", "987-875-5455", 2016)
# print("Volledige info boek 2")
# print(b2)
# Terminal:
# Titel van boek 1: Python for dummies
# Volledige info boek 1
# Louis Kegels , Python for dummies bis (Arco) *2019*
# Volledige info boek 2
# Johan Vannieuwenhuyse , Hoe leg ik een vijver in mijn tuin aan? Deel 1 (Aveve) *2016*

# Doe een import van het model
from modelweek07.Boek import Boek

# maak een nieuw boek aan
print("\n*******Nieuw boek aanmaken*******")
b1 = Boek("Python for dummies", "Louis Kegels", "Arco", "125-875-5455")

print(f"Titel van boek 1: {b1.titel}")
print("Volledige info boek 1")
print(b1)

# maak een tweede boek
print("\n*******Nieuw boek aanmaken*******")
print("Volledige info boek 2")
b2 = Boek("Hoe leg ik een vijver in mijn tuin aan? Deel 1",
"Johan Vannieuwenhuyse", "Aveve", "987-875-5455", 2016)
print(b2)