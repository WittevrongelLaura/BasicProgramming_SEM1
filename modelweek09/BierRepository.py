import json
from .Bier import Bier

class BierRepository:
    # privaat klasse-attribuut
    __filename = "docweek09/bieren.json"

    # static methodes

    # hulpmethode om json bestand te lezen
    @staticmethod
    def __read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)  # imports noodzakelijk

    @staticmethod
    def inlezen_bieren():
        resultaat = []
        # je krijgt een list van dictionaries terug
        list_bieren = BierRepository.__read_local_json_file(BierRepository.__filename)
        # print(list_bieren)
        # list van dictionaries
        for dict_bier in list_bieren:
            # bier aanmaken
            try:
                temp_naam = dict_bier["Naam"]
                temp_brouwerij = dict_bier["Brouwerij"]
                temp_kleur = dict_bier["Kleur"]
                temp_alcohol = float(dict_bier["alcohol"])
                nieuw_bier_object = Bier(temp_naam, temp_brouwerij, temp_alcohol, temp_kleur)
                # bier toevoegen aan resultaat
                resultaat.append(nieuw_bier_object)
            except ValueError as ex:
                print(f"Fout: {ex}")
        return resultaat

    @staticmethod
    def zoek_bieren_uit_brouwerij(list_met_bieren, zoekterm):
        resultaat = []

        for biertje in list_met_bieren:
            if zoekterm.lower() in biertje.naam.lower():
                resultaat.append(biertje)

        return resultaat