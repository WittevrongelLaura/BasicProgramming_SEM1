from .Tvprogramma import Tvprogramma
import random

class Zender:

    __aantal_aangemaakte_zenders = 0
    
    def __init__(self, parnaam, partaal):
        self.naam = parnaam
        self.taal = partaal
        self.programmas = []
        Zender.__aantal_aangemaakte_zenders += 1

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self):
        """ The naam property. """
        return self.__naam
    
    @naam.setter
    def naam(self, value):
        self.__naam = value
    
    # ********** property taal - (setter/getter) ***********
    @property
    def taal(self):
        """ The taal property. """
        return self.__taal
    
    @taal.setter
    def taal(self, value):
        if value == "NL" or value == "ENG" or value == "FR":
            self.__taal = value
        else:
            self.__taal = "ERROR"
    
    # ********** property programmas - (setter/getter) ***********
    @property
    def programmas(self):
        """ The programmas property. """
        return self.__programmas
    
    @programmas.setter
    def programmas(self, value):
        self.__programmas = value
    
    def __str__(self):
        return f"{self.naam} -> {self.programmas}"


    def voeg_programma_toe(self, programma):
        if type(programma) is Tvprogramma:
            self.programmas.append(programma)
    
    def zoek_afgelopen_programmas(self):
        lijst_afgelopen_programmas = []
        for programma in self.programmas:
            if programma.is_actief is False:
                if not programma in lijst_afgelopen_programmas:
                    lijst_afgelopen_programmas.append(programma)
        return lijst_afgelopen_programmas

    def selecteer_willekeurig_programma(self):
        return random.choice(self.programmas)

    @staticmethod
    def geef_aantal_aangemaakte_zenders():
        return Zender.__aantal_aangemaakte_zenders