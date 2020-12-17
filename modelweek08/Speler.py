from .Geboortedatum import Geboortedatum

class Speler:

    #class attributen die door alle objecten gedeeld worden
    naam_ploeg = ""
    __doelpunten_ploeg = 0

    # Constructor
    def __init__(self, parvoornaam, parnaam, partype, parwaarde=0, pareigendoelpunten=0, pargebdatum = Geboortedatum(1,1,1990)):
        self.naam = parnaam
        self.voornaam = parvoornaam
        self.type = partype
        self.waarde = parwaarde
        self.geboortedatum = pargebdatum
        # geen setter aangawezig => rechtstreeks data-attribuut instellen
        self.__aantal_eigen_doelpunten = pareigendoelpunten
        #vergeet niet: doelpunten van de ploeg moeten ook verhoogd worden
        Speler.__doelpunten_ploeg += pareigendoelpunten

    # Properties
    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if type(value) is str and value != "":
            self.__naam = value
        else:
            self.__naam = "onbekend"

    # ********** property voornaam - (setter/getter) ***********
    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        if type(value) is str and value != "":
            self.__voornaam = value
        else:
            self.__voornaam = "onbekend"

    # ********** property type - (setter/getter) ***********
    @property
    def type(self):
        """The type property."""
        return self.__type

    @type.setter
    def type(self, value):
        if type(value) is str and value.lower() in ['keeper', 'aanvaller', 'middenvelder', 'verdediger']:
            self.__type = value
        else:
            self.__type = "type ongeldig"

    # ********** property aantal_eigen_doelpunten - (enkel getter) ***********
    @property
    def aantal_eigen_doelpunten(self):
        """The aantal_doelpunten property."""
        return self.__aantal_eigen_doelpunten

    # ********** property waarde - (setter/getter) ***********
    @property
    def waarde(self):
        """ The waarde property. """
        return self.__waarde

    @waarde.setter
    def waarde(self, value):
        if type(value) is int and value >= 0:
            self.__waarde = value
        else:
            self.__waarde = -1  # -1 heeft vaak de betekenis van een foutieve waarde


    # ********** property geboortedatum - (setter/getter) ***********
    @property
    def geboortedatum(self):
        """ The geboortedatum property. """
        return self.__geboortedatum
    
    @geboortedatum.setter
    def geboortedatum(self, value):
        if type(value) is Geboortedatum:
            self.__geboortedatum = value
        else:
            self.__geboortedatum = Geboortedatum(1,1,1990)
    
    


    # ToString

    def __str__(self):
        return f"speler {self.naam}, {self.voornaam} ({self.waarde}/10) doelpunten: {self.aantal_eigen_doelpunten}"

    #repr-methode
    #wordt gebruikt om objecten in een list af te printen
    def __repr__(self):
        return f"speler {self.naam}, {self.voornaam} ({self.waarde}/10)"

    def maak_doelpunt(self):
        #eigen aantal verhogen
        self.__aantal_eigen_doelpunten += 1
        #doelpunten van ploeg verhogen met 1
        Speler.__doelpunten_ploeg += 1

    #heeft geen self parameter
    #methode dat je rechtstreeks op de klasse kan uitvoeren
    #methode is dus niet gebonden aan een object
    @staticmethod
    def get_doelpunten_saldo_ploeg():
        return Speler.__doelpunten_ploeg