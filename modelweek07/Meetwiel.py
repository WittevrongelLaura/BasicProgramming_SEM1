import math

class Meetwiel:
    def __init__(self, parstraal=0, paromwentelingen=0):
        self.straal = parstraal
        self.omwentelingen = paromwentelingen

    @property
    def straal(self):
        """ The straal property. """
        return self.__straal
    
    @straal.setter
    def straal(self, value):
        if type(value) is float and value >= 0:
            self.__straal = value
        else:
            self.__straal = 0
    
    @property
    def omwentelingen(self):
        """ The omwentelingen property. """
        return self.__omwentelingen
    
    @omwentelingen.setter
    def omwentelingen(self, value):
        self.__omwentelingen = value
    
    @property
    def omtrek(self):
        """ The omtrek property. """
        #is een berekende property
        #heeft geen eigen private attibute
        return self.straal * 2 * math.pi
    
    @property
    def afstand(self):
        """ The afstand property. """
        #als ik kan kiezen verkies ik de getter ipv private property
        return self.omtrek * self.omwentelingen
    
    

    def __str__(self):
        return f"Meetwiel met straal {self.straal} en omwentelingen {self.omwentelingen}"