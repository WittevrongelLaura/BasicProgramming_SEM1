import json
from .MakeUpProduct import MakeUpProduct
from .ProductColor import ProductColor

class MakeUpRepository:
    # privaat klasse-attribuut
    __filename = "docweek09/makeupproducts.json"

    # static methodes

    # hulpmethode om json bestand te lezen
    @staticmethod
    def __read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)  # imports noodzakelijk

    @staticmethod
    def load_products():
        all_products = []
        list_van_dict = MakeUpRepository.__read_local_json_file(MakeUpRepository.__filename)

        for dict_product in list_van_dict:
            try:
                #haal de geg op uit de dict
                id = int(dict_product["id"])
                brand = dict_product["brand"]
                name = dict_product["name"]
                price = float(dict_product["price"])
                product_link = dict_product["product_link"]
                
                #maak een object aan vh type MakeUpProduct (gebruik de constructor)
                temp_product = MakeUpProduct(id, brand, name, price, product_link)
                
                list_kleuren = dict_product["product_colors"] # <= list van dict
                for kleur in list_kleuren:
                    temp_kleur = ProductColor(kleur["colour_name"], kleur["hex_value"])
                    temp_product.add_productcolor(temp_kleur)

                #voeg die toe aan list all_products
                all_products.append(temp_product)
            except ValueError as ex:
                print(f"Foutje: {ex}")
            except TypeError as ex:
                print(f"TypeError {ex}")
        
        return all_products


    @staticmethod
    def search_in_products(list_producten, searchterm):
        lst = []
        for product in list_producten:
            if searchterm.lower() in product.name.lower():
                lst.append(product)

        return lst