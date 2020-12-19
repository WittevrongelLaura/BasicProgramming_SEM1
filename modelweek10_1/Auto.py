from .Persoon import Persoon


class Auto:

    def __init__(self, par_nummerplaat, par_eigenaar):
        self.nummerplaat = par_nummerplaat
        self.eigenaar = par_eigenaar

    # ********** property nummerplaat - (setter/getter) ***********  
    @property
    def nummerplaat(self):
        """The nummerplaat property."""
        return self.__nummerplaat

    @nummerplaat.setter
    def nummerplaat(self, value):
        if value != "":
            self.__nummerplaat = value
        else:
            raise ValueError("Geen geldige nummerplaat!")

    # ********** property eigenaar - (setter/getter) ***********  
    @property
    def eigenaar(self):
        """The eigenaar property."""
        return self.__eigenaar

    @eigenaar.setter
    def eigenaar(self, value):
        # if type(value) is Persoon:        #WERKT NIET (door de overerving)
        if isinstance(value,Persoon):
            self.__eigenaar = value
        else:
            raise ValueError("Geen geldige eigenaar")

    def __str__(self):
        return f"Voertuig met kenteken {self.nummerplaat} heeft als eigenaar: {self.eigenaar}"
