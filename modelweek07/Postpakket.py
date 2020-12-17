class Postpakket:
    def __init__(self, paromschrijving, parbreedte, parhoogte, pardiepte):
        self.__omschrijving = paromschrijving
        self.breedte = parbreedte
        self.hoogte = parhoogte
        self.diepte = pardiepte
        

    @property
    def omschrijving(self):
        """ The omschrijving property. """
        return self.__omschrijving
    
    @property
    def breedte(self):
        """ The breedte property. """
        return self.__breedte
    
    @breedte.setter
    def breedte(self, value):
        if type(value) is int and value > 0:
            self.__breedte = value
        else:
            self.__breedte = 1
    
    @property
    def hoogte(self):
        """ The hoogte property. """
        return self.__hoogte
    
    @hoogte.setter
    def hoogte(self, value):
        if type(value) is int and value > 0:
            self.__hoogte = value
        else:
            self.__hoogte = 1
    
    @property
    def diepte(self):
        """ The diepte property. """
        return self.__diepte
    
    @diepte.setter
    def diepte(self, value):
        if type(value) is int and value > 0:
            self.__diepte = value
        else:
            self.__diepte = 1
    
    @property
    def volume(self):
        """ The volume property. """
        self.__volume = self.__breedte * self.__hoogte * self.__diepte
        return self.__volume
    
    

    def __str__(self):
        return f"Pakketje: {self.omschrijving} ({self.breedte} cm * {self.hoogte} cm * {self.diepte} cm)"