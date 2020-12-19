# Oef 02
# Neem oefening 2 uit week9 (Make-up oefening) of gebruik het bronmateriaal.
# Integreer verschillende log-berichten:
# • in de verschillende setter-methodes waar er inputvalidatie plaats vindt: log de verkeerd
# doorgegeven waarde;
# • in de methode ‘load_products’:
# o log het aangemaakte MakeupProduct-object;
# o log op het einde het aantal ingelezen objecten.

from modelweek11.MakeUpProduct import MakeUpProduct
from modelweek11.MakeUpRepository import MakeUpRepository
import logging

#logging
logging.basicConfig(filename="docweek11/makeUpLog.log", level=logging.INFO)

list_products = MakeUpRepository.load_products()
list_products.sort()
print(f"Aantal ingelezen make-up producten: {len(list_products)}")

#voorbeeld: primer
zoekterm = input("Geef een deel van de naam op:> ")
results = MakeUpRepository.search_in_products(list_products, zoekterm)
print("Dit zijn de gevonden producten: ")
for product in results:
    print(product)
