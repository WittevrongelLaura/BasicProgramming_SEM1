import json

# Neem deze code NIET over. Dit is enkel om de structuur van de json-file te verkennen en te testen.

#hulpmethode om json bestand te lezen
def __read_local_json_file(bestandsnaam):
    fo = open(bestandsnaam, encoding="utf8")
    response_json = fo.read()
    fo.close()
    return json.loads(response_json)#imports noodzakelijk


def test_bieren():
    list_bieren = __read_local_json_file("docweek09/bieren.json")  # je krijgt een list van dictionaries terug
    #print(list_bieren)
    # list van dictionaries
    for dict_bier in list_bieren:
        print(f"Nummer: {dict_bier['Nr']}")
        print(f"Naam: {dict_bier['Naam']}")
        print(f"Brouwerij: {dict_bier['Brouwerij']}")
        print(f"Kleur: {dict_bier['Kleur']}")
        input("druk op enter voor volgende bier...")


def test_makeup():
    list_producten = __read_local_json_file(
        "doc/makeupproducts.json")  # je krijgt een dict terug
    # list van dictionaries
    for dict_product in list_producten:
        print(f"Id: {dict_product['id']}")
        print(f"Merk: {dict_product['brand']}")
        print(f"Naam: {dict_product['name']}")
        print(f"Prijs: {dict_product['price']}")
        print(f"Link: {dict_product['product_link']}")

        # kleuren opvragen: list van dictionaries
        list_kleuren = dict_product["product_colors"]

        print("Beschikbare kleuren:")
        for dict_kleur in list_kleuren:
            print(f"\t- {dict_kleur['colour_name']}")

        input("druk op enter voor volgende product...")

test_bieren()
# test_makeup()
