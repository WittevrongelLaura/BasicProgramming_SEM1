# Oef 06
# Oef: maak een dataklasse Winkelkar die als private attribuut een list van producten
# (String) bijhoudt. Voorzie de klasse van volgende methodes:
# • Programmeer de constructor: methode __init__()
# o Deze methode maakt altijd een lege winkelkar aan en heeft dus geen
# parameters.
# De producten worden voorgesteld als een lege list in een private attribuut.
# • Programmeer de methode __str__()
# • Een getter property-methode ‘producten’ die de lijst terug geeft
# • Methode ‘voeg_product_toe(nieuw_product)’ die aan het winkelkarretje een
# nieuw product toevoegt.
# • Methode ‘verwijder_product(product)’ die uit het winkelkarretje een product
# verwijdert.
# o Wat gebeurt er als je een product wil verwijderen die niet bestaat? Hoe
# kan je dit vermijden?
# Test volgende code uit. Je kan hiervoor het testbestand op Leho gebruiken.
# • Maak 2 winkelkarretjes aan. Voeg verschillende producten aan elk toe. Print
# nadien beide af.
# from model.Winkelkar import Winkelkar
# action_kar = Winkelkar()
# action_kar.voeg_product_toe("cd1")
# action_kar.voeg_product_toe("cd2")
# action_kar.voeg_product_toe("cd3")
# action_kar.voeg_product_toe("cd4")
# action_kar.verwijder_product("cd3")
# ikea_kar = Winkelkar()
# ikea_kar.voeg_product_toe("Billy")
# ikea_kar.voeg_product_toe("Factum")
# print(f"Winkelkar 1: {action_kar}")
# print(f"Winkelkar 2: {ikea_kar}")
# Terminal
# Winkelkar 1: De winkelkar bestaat uit 3: ['cd1', 'cd2', 'cd4']
# Winkelkar 2: De winkelkar bestaat uit 2: ['Billy', 'Factum']

from modelweek07.Winkelkar import Winkelkar

action_kar = Winkelkar()
action_kar.voeg_product_toe("cd1")
action_kar.voeg_product_toe("cd2")
action_kar.voeg_product_toe("cd3")
action_kar.voeg_product_toe("cd4")
action_kar.verwijder_product("cd5")

ikea_kar = Winkelkar()
ikea_kar.voeg_product_toe("Billy")
ikea_kar.voeg_product_toe("Factum")

print(f"Winkelkar 1: {action_kar}\n")
print(f"Winkelkar 2: {ikea_kar}\n")

