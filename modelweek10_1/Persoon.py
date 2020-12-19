from datetime import datetime


class Persoon:

    # class attributes (géén self!)
    vereniging = "Howest"
    __aantal_personen = 0

    def __init__(self, par_naam, par_voornaam, par_geboortejaar=2020):
        self.naam = par_naam
        self.voornaam = par_voornaam
        self.geboortejaar = par_geboortejaar
        Persoon.__aantal_personen += 1

    def __del__(self):
        Persoon.__aantal_personen -= 1

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self):
        """ The naam property. """
        return self.__naam

    @naam.setter
    def naam(self, value):
        if value != "":
            self.__naam = value
        else:
            raise ValueError("een lege naam is niet toegestaan!")

    # ********** property voornaam - (setter/getter) ***********
    @property
    def voornaam(self):
        """ The voornaam property. """
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        if value != "" and value.isalpha():
            self.__voornaam = value
        else:
            # self.__voornaam = "onbekend"
            raise ValueError("een lege voornaam is niet toegestaan!")

    # ********** property geboortejaar - (setter/getter) ***********
    @property
    def geboortejaar(self):
        """ The geboortejaar property. """
        return self.__geboortejaar

    @geboortejaar.setter
    def geboortejaar(self, value):
        if type(value) is int:
            self.__geboortejaar = value
        else:
            # self.__geboortejaar = -1
            raise ValueError("Geen geldige geboortedatum!")

    # Calcultated property
    @property
    def leeftijd(self):
        """ The leeftijd property. """
        verschil = datetime.now().year - self.geboortejaar
        return verschil

    def __str__(self):
        return f"{self.naam.upper()} {self.voornaam}"

    def __repr__(self):
        return f"Persoon: {self.naam.upper()} {self.voornaam} ({self.geboortejaar})"

    # equals-operator
    def __eq__(self, other):
        if self.naam == other.naam and self.voornaam == other.voornaam and self.geboortejaar == other.geboortejaar:
            return True
        else:
            return False

    # lower-then operator: we overschrijven de < operator
    # sorteren op leeftijd.
    # bij zelfde leeftijd: sorteren op naam
    def __lt__(self, other):
        if self.leeftijd != other.leeftijd:
            if self.leeftijd < other.leeftijd:
                return True
            else:
                return False
        else:
            if self.naam < other.naam:
                return True
            else:
                return False

    # static-methodes zetten we onderaan
    @staticmethod
    def geef_aantal_personen():
        return Persoon.__aantal_personen
