class Bier:
    #init-methode (constructor)
    def __init__(self, parnaam, parbrouwerij, paralcoholpercentage, parkleur):
        self.naam = parnaam
        self.brouwerij = parbrouwerij
        self.alcoholpercentage = paralcoholpercentage
        self.kleur = parkleur

    # properties

    @property
    def naam(self):
        """ The naam property. """
        return self.__naam.upper()  # biernaam in hoofdletters weergeven

    @naam.setter
    def naam(self, value):
        if value != "":
            self.__naam = value
        else:
            self.__naam = "onbekend"

    @property
    def brouwerij(self):
        """ The brouwerij property. """
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        if value != "":
            self.__brouwerij = value
        else:
            self.__brouwerij = "onbekend"

    @property
    def alcoholpercentage(self):
        """ The alcoholpercentage property. """
        return self.__alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, value):
        if type(value) is float and value >= 0 and value <= 100:
            self.__alcoholpercentage = value
        else:
            self.__alcoholpercentage = -1

    @property
    def kleur(self):
        """ The kleur property. """
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        if value != "":
            self.__kleur = value
        else:
            self.__kleur = "onbekend"

    #toString-methode (str)

    def __str__(self):
        return f"{self.naam} {self.brouwerij} - {self.alcoholpercentage}"
