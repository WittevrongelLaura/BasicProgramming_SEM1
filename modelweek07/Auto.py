class Auto:
    def __init__(self, parmerk, parmodel, parkleur="grijs", parbrandstof = "diesel"):
        self.__merk = parmerk
        self.__model = parmodel
        self.kleur = parkleur
        self.__brandstof = parbrandstof
        self.kmstand = 0

    @property
    def merk(self):
        """ The merk property. """
        return self.__merk

    @property
    def model(self):
        """ The model property. """
        return self.__model

    @property
    def kleur(self):
        """ The kleur property. """
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value

    @property
    def brandstof(self):
        """ The brandstof property. """
        return self.__brandstof.lower()

    @property
    def kmstand(self):
        """ The kmstand property. """
        return self.__kmstand

    @kmstand.setter
    def kmstand(self, value):
        if type(value) is int and value >= 0:
            self.__kmstand = value
        else:
            self.__kmstand = -1

    def rijden(self, extra_km):
        #ik moet de km stand verhogen
        self.kmstand += extra_km 

    def maak_lawaai(self):
        #hoe kan ik weten welk type auto?
        if self.brandstof == "diesel":
            return "bwaaaaaahrooooah"
        elif self.brandstof == "benzine":
            return "swoooooohsj"
        elif self.brandstof == "elektrisch":
            return "sssssssst"
        else:
            return "panne"

    def __str__(self):
        return f"{self.merk} (model: {self.model} kleur: {self.kleur})"
