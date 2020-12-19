from .Ouder import Ouder
from .Student import Student
import json
import random

class PersoonRepository:

    __filename = "docweek10_1/personen.json"

    @staticmethod
    def __read_local_json_file():
        fo = open(PersoonRepository.__filename, encoding="utf8")
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def inlezen_ouders_met_studenten():
        #? wat geeft de functie terug??? List van objecten v h type Ouder
        list_res = []
        list_json = PersoonRepository.__read_local_json_file()

        #elke dict overlopen in de list van dict
        for dict_ouder in list_json:
            try:
                naam_ouder = dict_ouder["Naam"]
                voornaam_ouder = dict_ouder["Voornaam"]
                geboorte_ouder = int(dict_ouder["Geboortejaar"])
                list_studenten = dict_ouder["Studenten"] #<-- geeft een list van dict

                # maak je een object vh type ouder 
                temp_ouder = Ouder(naam_ouder, voornaam_ouder, geboorte_ouder)
                for dict_kind in list_studenten:
                    # haal geg op v d student
                    naam_student = dict_kind["Naam"]
                    voornaam_student = dict_kind["Voornaam"]
                    geboorte_student = int(dict_kind["Geboortejaar"])
                    opleiding_student = dict_kind["Opleiding"]
                    nummer = random.randint(1,10000)

                    # maak een nieuw object vh type student
                    temp_kind = Student(naam_student, voornaam_student, nummer, opleiding_student, geboorte_student)

                    # voeg student toe aan de ouder
                    temp_ouder.voeg_student_toe(temp_kind)
                # voeg je deze toe aan list_res
                list_res.append(temp_ouder)
            except Exception as ex:
                print(f"Foutmelding bij het inlezen: {ex}")

        return list_res

    @staticmethod
    def filter_ouders_met_studenten_uit_opleiding(list_ouders, naam_opleiding):
        list_res = []
        # overloop alle ouder objecten
        for ouder in list_ouders:
            # overloop alle kinderen van 1 ouder
            for student in ouder.studenten:
                #haal via de get property van 1 kind (studenten) zijn op leiding op
                if student.opleiding.lower() == naam_opleiding.lower():
                    list_res.append(ouder)

            return list_res