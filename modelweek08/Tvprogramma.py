from .Presentator import Presentator

class Tvprogramma:
    def __init__(self, partitel, parpresentator):
        self.__titel = partitel
        self.presentator = parpresentator
        self.is_actief = True

    # ********** property titel - (setter/getter) ***********
    @property
    def titel(self):
        """ The titel property. """
        return self.__titel

    
    # ********** property presentator - (setter/getter) ***********
    @property
    def presentator(self):
        """ The presentator property. """
        return self.__presentator
    
    @presentator.setter
    def presentator(self, value):
        if type(value) is Presentator:
            self.__presentator = value
        else:
            self.__presentator = "ERROR"
    
    # ********** property is_actief - (setter/getter) ***********
    @property
    def is_actief(self):
        """ The is_actief property. """
        return self.__is_actief
    
    @is_actief.setter
    def is_actief(self, value):
        if type(value) is bool:
            self.__is_actief = value
        else: 
            self.__is_actief = False
    
    def __str__(self):
        return f"TV Programma: {self.titel} door {self.presentator}"

    def __repr__(self):
        return f"TV Programma: {self.titel} door {self.presentator}"