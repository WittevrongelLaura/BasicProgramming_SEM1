class Voertuig:
    #klasse attribuut
    __aantal_voertuigen = 0

    def __init__(self, id, merk, bouwjaar, kmstand):
        self.__id = id
        self.__merk = merk
        self.__bouwjaar = bouwjaar
        self.kmstand = kmstand
        self.reisbestemming = ""
        #verhoog het klasse attribuut
        Voertuig.__aantal_voertuigen += 1

    #als een object wordt verwijerd
    def __del__(self):
        #verlaag het aantal voertuigen
        Voertuig.__aantal_voertuigen -= 1

    # ********** property id - (setter/getter) ***********
    @property
    def id(self):
        """ The id property. """
        return self.__id
    
    # ********** property merk - (setter/getter) ***********
    @property
    def merk(self):
        """ The merk property. """
        return self.__merk.upper()
    
    # ********** property bouwjaar - (setter/getter) ***********
    @property
    def bouwjaar(self):
        """ The bouwjaar property. """
        return self.__bouwjaar
    
    # ********** property kmstand - (setter/getter) ***********
    @property
    def kmstand(self):
        """ The kmstand property. """
        return self.__kmstand
    
    @kmstand.setter
    def kmstand(self, value):
        if type(value) is int or type(value) is float:
            self.__kmstand = value
        else:
            raise ValueError("Fout kmstand")
    
    # ********** property reisbestemming - (setter/getter) ***********
    @property
    def reisbestemming(self):
        """ The reisbestemming property. """
        return self.__reisbestemming
    
    @reisbestemming.setter
    def reisbestemming(self, value):
        if type(value) is str:
            self.__reisbestemming = value
        else:
            raise ValueError("Reisbestemming is geen string!")
    
    def __str__(self):
        return f"{self.merk} {self.bouwjaar}"

    def __repr__(self):
        return f"{self.merk} {self.bouwjaar}"

    def __eq__(self, other):
        if self.id == other.id:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__kmstand < other.__kmstand:
            return True
        else:
            return False


    @staticmethod
    def geef_aantal_voertuigen():
        return Voertuig.__aantal_voertuigen