# Oef 03
# Voor deze oefening maken we gebruik van een json-file afkomstig van een webservice
# (https://makeup-api.herokuapp.com/) Deze webservice laat de gebruiker toe
# informatie over talrijke make-up producten op te vragen. Afhankelijk van de interesse
# kan men de zoekopdracht verfijnen tot een specifiek producttype en/of subcategorie.
# Hoe verfijnder de zoekopdracht, hoe sneller het antwoord binnenkomt. Bijvoorbeeld,
# volgende link geeft enkel info over lipsticks terug.
# https://makeupapi.
# herokuapp.com/api/v1/products.json?product_category=lipstick&product_type=li
# pstick
# In het bronmateriaal vind je ‘makeupproducts.json’ met het resultaat van
# bovenstaande zoekopdracht terug. (het staat je vrij om de inhoud te vervangen door
# het resultaat van een andere zoekopdracht).
# Bestudeer aandachtig het json-bestand, en vervolledig volgende uitspraken.
# • Het resultaat van de json is een ………..…...[] van ……………{}
# • Elke …..{} bestaat uit keys en values én stellen een mackup artikel voor.
# o De key product_colors is speciaal, deze bestaat uit een …… [] van …..{}
# ->
# Week 09
# Basic Programming (skills) / 10
# Voor deze oefening wensen we van elk product volgende informatie bij te houden:
# - id
# - brand
# - name
# - price
# - product_link
# - product_colors
# Merk op dat voor de elk beschikbaar productkleur volgende info wordt getoond:
# hex_value en een color_name.
# Doel: inlezen van het json-bestand waarbij een lijst van producten wordt aangemaakt.
# In elk product zit een lijst met beschikbare productkleuren.
# Werkwijze:
# 1: Plaast het json-bestand in de submap ‘doc’.
# Verken het json bestand eens via verkenning_json.py. Dit bestand heb je straks niet
# meer nodig, maar dient enkel om je de keys en values eigen te maken.
# 2: In de submap ‘model’ maken we volgende twee dataklasses aan:
# 2a: klasse ‘ProductColor’ met de attributen colorname en hexvalue. Voorzie de klasse
# van een constructor, properties, tostring-methode, repr-methode, eq-methode
# 2b: klasse ‘MakeUpProduct’ met de attributen id, brand, name, price, productlink en
# colors aan.
# - De klassieke methodes__init__() met parameters id, brand, name, price,
# productlink
# - Voor de colors maak je een lege list aan in de init-methode. Je voorziet voor dit
# attribuut enkel een get-property. Voor de andere attributen voorzie je een
# get&set property.
# - Voeg een methode ‘add_productcolor’ toe: deze methode heeft één
# parameter, nl een object van de klasse ProductColor. Deze methode voegt het
# object aan de lijst met colors toe.
# o Controleer in de methode of de parameter weldegelijk een object van
# de klasse ProductColor is.
# o Controleer of de parameter niet in de list al aanwezig is.
# (welke methode uit de klasse ProductColor wordt hiervoor achter de
# schermen gebruikt?)
# - Programmeer ook de methode __str__(): deze geeft terug:
# name (brand) -> Available Colors: aantal_beschikbare_kleuren
# 3: Voeg een nieuw bestand MakeUpRepository.py in de map ‘model’ toe. Maak hierin
# een nieuwe klasse MakeUpRepository aan.
# Week 09
# Basic Programming (skills) / 11
# • Voorzie de klasse van een private klasse-attributte “__filename” die het pad
# naar het bronbestand bijhoudt. Bijvoorbeeld:
# __filename = "doc/makeupproducts.json"
# • Voeg een static methode ‘load_products’ toe die in staat is om het
# bronbestand in te lezen en een list van producten terug te geven.
# Om een lokaal json-file in te lezen maak je gebruik van volgende private
# hulpfunctie:
# • Deze hulpmethode geeft een list terug, met dictionaries. Elk element (dictionary)
# bevat informatie voor één MakeUpProduct. Overloop nu alle elementen. Elk
# element is een dictionary waarmee je specifieke informatie kan opvragen.
# Vraag via de juiste key (let op hoofdletters) elke waarde op. Maak met alle info
# een object van de klasse MakeUpProduct. Opgelet: niet elke vermelde waarde is
# correct. Gebruik daarom exception handling.
# Test de methode voldoende uit in een test-bestand ‘test_makeup.py’, vergeet niet de
# correcte klassen te importeren
# 4: Voeg een static methode ‘search_in_products’ toe aan MakeUpRepository met
# twee parameters, nl. een list van objecten van de klasse MakeUpProduct én een deel
# van een productnaam. Doorloop alle objecten uit de list en geef enkel deze terug
# waarvan de productnaam het gezochte deel bevat.
# Voordat je de producten toont, sorteer je de volledig lijst van MakeUpProducten.
# Producten met het minst aantal kleuren staan vooraan in de lijst.
# Vervolledig ‘test_makeup.py’, om volgende output.

from modelweek09.MakeUpProduct import MakeUpProduct
from modelweek09.MakeUpRepository import MakeUpRepository


list_products = MakeUpRepository.load_products()
list_products.sort()
print(f"Aantal ingelezen make-up producten: {len(list_products)}")

#voorbeeld: primer
zoekterm = input("Geef een deel van de naam op:> ")
results = MakeUpRepository.search_in_products(list_products, zoekterm)
print("Dit zijn de gevonden producten: ")
for product in results:
    print(product)
