class Presentator:
    def __init__(self, parnaam, parvoornaam):
        self.naam = parnaam
        self.voornaam = parvoornaam

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self):
        """ The naam property. """
        return self.__naam

    @naam.setter
    def naam(self, value):
        self.__naam = value

    # ********** property voornaam - (setter/getter) ***********
    @property
    def voornaam(self):
        """ The voornaam property. """
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        self.__voornaam = value

    def __str__(self):
        return f"presentator: {self.naam}, {self.voornaam}"

    def __repr__(self):
        return f"presentator: {self.naam}, {self.voornaam}"

    def __eq__(self, other):
        if self.naam == other.naam and self.voornaam == other.voornaam:
            return True
        else:
            return False
