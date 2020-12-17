from .Tvprogramma import Tvprogramma
from random import random

class Zender:
    __aantal_afgelopen_programmas = 0

    def __init__(self, parnaam, partaal):
        self.naam = parnaam
        self.taal = partaal
        self.programmas = []

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
        if programma in Tvprogramma.titel:
            self.programmas.append(programma)
    
    def zoek_afgelopen_programmas(self):
        pass

    def selecteer_willekeurig_programma(self):
        return random.choice(self.programmas)

    @staticmethod
    def geef_aantal_aangemaakte_zenders():
        return Zender.__aantal_afgelopen_programmas