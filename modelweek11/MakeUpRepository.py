import json, logging
from .MakeUpProduct import MakeUpProduct
from .ProductColor import ProductColor


class MakeUpRepository:
    # privaat klasse-attribuut
    __filename = "docweek11/makeupproducts.json"

    #static-methodes
    @staticmethod
    def __read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)        #imports noodzakelijk

    @staticmethod
    def load_products():
        resultaat = []      #hierin komen objecten van de klasse MakeUpProduct
        list_producten = MakeUpRepository.__read_local_json_file(MakeUpRepository.__filename)

        #list overlopen: de ingelezen list bestaat uit dictionaries
        for dict_product in list_producten:
            try:
                # haal alle info op: id, name, price, brand, productlink
                id = dict_product["id"]
                name = dict_product["name"]
                brand = dict_product["brand"]
                price = float(dict_product["price"])
                productlink = dict_product["product_link"]

                # maak een object aan van de klasse MakeUpProduct
                nieuw_product = MakeUpProduct(id, brand, name, price, productlink)
                

                #kleuren ook registreren
                #ophalen via de key --> opnieuw een list van dictionaries!!
                list_colors = dict_product["product_colors"]
                for dict_color in list_colors:
                    hexvalue = dict_color["hex_value"]
                    colorname = dict_color["colour_name"]
                    #object aanmaken van de klasse ProductColor
                    new_productcolor = ProductColor(colorname, hexvalue)
                    #toevoegen aan eerder aangemaakt make-up product
                    nieuw_product.add_productcolor(new_productcolor)

                #voeg toe aan de list
                resultaat.append(nieuw_product)
                logging.debug(f"Nieuw product {nieuw_product.name} toegevoegd")
            except Exception as ex:
                logging.error(f"Value-error: {ex}")
                print(f"Value-error: {ex}")
        return resultaat

    @staticmethod
    def search_in_products(listproducts, searchname):
        zoekresultaat = []
        #doorloop de list van objecten van de klasse MakeUpProduct
        #ga op zoek waar de gezochte naam in de officiële naam voorkomt
        for product in listproducts:
            if searchname.lower() in product.name.lower():
                zoekresultaat.append(product)
        
        #geen zoekresultaat terug
        return zoekresultaat



