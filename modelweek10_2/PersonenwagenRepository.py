import json
from .Personenwagen import Personenwagen

class PersonenwagenRepository:
    __filename = "docweek10_2/auto.json"

    @staticmethod
    def __read_local_json_file():
        fo = open(PersonenwagenRepository.__filename, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def inlezen_personenwagens():
        list_res = []
        list_json = PersonenwagenRepository.__read_local_json_file()

        for auto in list_json:
            try:
                id = auto["Auto-id"]
                merk = auto["Merk"]
                bouwjaar = auto["Bouwjaar"]
                kmstand = auto["Km-stand"]
                max_plaatsen = auto["Max-plaatsen"]

                temp_auto = Personenwagen(id, merk, bouwjaar, kmstand, max_plaatsen)

                list_res.append(temp_auto)

            except Exception as ex:
                print(f"Fout bij inlezen: {ex}")

        return list_res

    @staticmethod
    def zoek_wagen(list_personenwagen, id_auto):
    
        for auto in list_personenwagen:
            if auto.id == id_auto:
                return auto

         