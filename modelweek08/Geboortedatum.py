import random
from datetime import datetime

class Geboortedatum:
    __aantal_geboortedata = 0

    def __init__(self, pardag, parmaand, parjaar):
        self.__dag = pardag
        self.__maand = parmaand
        self.__jaar = parjaar
        Geboortedatum.__aantal_geboortedata += 1

    def __del__(self):
        #is het omgekeerde van init
        #wowrdt uitgevoerd als 
        pass

    # ********** property dag - (setter/getter) ***********
    @property
    def dag(self):
        """ The dag property. """
        return self.__dag
    
    @dag.setter
    def dag(self, value):
        if value >= 1 and value <= 31:
            self.__dag = value
        else:
            self.__dag = -1
    
    # ********** property maand - (setter/getter) ***********
    @property
    def maand(self):
        """ The maand property. """
        return self.__maand
    
    @maand.setter
    def maand(self, value):
        # of range(1,13) gebruiken
        if value >= 1 and value <= 12:
            self.__maand = value
        else:
            self.__maand = -1
    
    # ********** property jaar - (setter/getter) ***********
    @property
    def jaar(self):
        """ The jaar property. """
        return self.__jaar
    
    @jaar.setter
    def jaar(self, value):
        if value >= 0:
            self.__jaar = value
        else:
            self.__jaar = -1
    
    def __str__(self):
        return f"{self.dag}/{self.maand}/{self.jaar}"

    def __eq__(self, other):
        if self.dag == other.dag and self.maand == other.maand and self.jaar == other.jaar:
            return True
        else:
            return False

    def __repr__(self):
        return f"Geboortedatum: {self.dag}/{self.maand}/{self.jaar}"

    def zelfde_verjaardag(self, andere_geboortedatum):
        if self.dag == andere_geboortedatum.dag and self.maand == andere_geboortedatum.maand:
            return True
        else:
            return False

    #public static methode (aanspreekbaar vanuit de testklasse)
    #zal toegang geven tot onze private klasse attribuut
    @staticmethod
    def geef_aantal_geboortedatums():
        return Geboortedatum.__aantal_geboortedata

    @staticmethod
    def genereer_willekeurige_verjaardag():
        jaar = random.randint(1950, datetime.now().year)
        maand = random.randint(1,12)
        dag = random.randint(1,31)#er wordt hier geen controle gedaan op het max van die maand
        nieuwe_verjaardag = Geboortedatum(dag,maand,jaar)
        return nieuwe_verjaardag

    @staticmethod
    def genereer_lijst_verjaardagen(aantal):
        verjaardagen = []
        for teller in range(0, aantal):
            temp_geb = Geboortedatum.genereer_willekeurige_verjaardag()
            verjaardagen.append(temp_geb)
        return verjaardagen