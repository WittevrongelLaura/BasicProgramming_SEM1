class Bier:

    # Constructor
    def __init__(self, parnaam, parbrouwerij, paralcoholpercentage, parkleur):
        # hieronder maken we gebruik van de properties!
        self.naam = parnaam
        self.brouwerij = parbrouwerij
        self.alcoholpercentage = paralcoholpercentage
        self.kleur = parkleur

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self):
        return self.__naam.upper()

    @naam.setter
    def naam(self, value):
        if value != "":
            self.__naam = value
        else:
            #self.__naam = "onbekend"
            #raise : terugwerpen vanwaar hij komt
            raise ValueError("Foutieve biernaam!")

    # ********** property brouwerij - (setter/getter) ***********
    @property
    def brouwerij(self):
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        if value != "":
            self.__brouwerij = value
        else:
            #self.__brouwerij = "onbekend"
            raise ValueError("Foutieve brouwerij!")


    # ********** property alcoholpercentage - (setter/getter) ***********
    @property
    def alcoholpercentage(self):
        return self.__alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, value):
        if type(value) is float and value >= 0 and value <= 100:
            self.__alcoholpercentage = value
        else:
            #self.__alcoholpercentage = -1
            raise ValueError("Foutief alcoholpercentage!")

    # ********** property kleur - (setter/getter) ***********
    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        if value != "":
            self.__kleur = value
        else:
            #self.__kleur = "onbekend"
            raise ValueError("Foutieve kleurwaarde!")

    # toString
    def __str__(self):
        return f"{self.naam} {self.brouwerij} - {self.alcoholpercentage}"

    def __repr__(self):
        return f"{self.naam} ({self.alcoholpercentage})"

    def __lt__(self, other):
        if self.alcoholpercentage < other.alcoholpercentage:
            return True
        else:
            return False 