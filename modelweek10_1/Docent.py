from .Persoon import Persoon


class Docent(Persoon):
    def __init__(self, parnaam, parvoornaam, parpersoneelsnummer, pargeboortejaar=2016):
        super().__init__(parnaam, parvoornaam, pargeboortejaar)
        self.personeelsnummer = parpersoneelsnummer
        self.__opleidingen = []  # list: in welke opleidingen geeft hij/zij les?

    # ********** property personeelsnummer - (setter/getter) ***********  
    @property
    def personeelsnummer(self):
        return self.__personeelsnummer

    @personeelsnummer.setter
    def personeelsnummer(self, value):
        if type(value) is int:
            self.__personeelsnummer = value
        else:
            raise ValueError("Geen geldig personeelsnummer!")
    
    # ********** property opleidingen - (enkel getter) ***********
    @property
    def opleidingen(self):
        return self.__opleidingen


    def __str__(self):
        return "Docent " + super().__str__()

    def __eq__(self, other):
        print("eq - Docent")
        if (self.__personeelsnummer == other.__personeelsnummer):
            return True
        else:
            return False

    def geeft_les_in(self, opleiding):
        if not opleiding in self.__opleidingen:
            self.__opleidingen.append(opleiding)

