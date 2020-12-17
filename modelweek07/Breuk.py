import math

class Breuk:

    def __init__(self, parrteller, parrnoemer):
        self.teller = parrteller
        self.noemer = parrnoemer

    @property
    def teller(self):
        """ The teller property. """
        return self.__teller

    @teller.setter
    def teller(self, value):
        self.__teller = value

    @property
    def noemer(self):
        """ The noemer property. """
        return self.__noemer

    @noemer.setter
    def noemer(self, value):
        self.__noemer = value

    def vereenvoudig(self):
        return math.gcd(self.teller, self.noemer)

    def __add__(self, other):
        pass 

    def __str__(self):
        return f"{self.teller} / {self.noemer}"
