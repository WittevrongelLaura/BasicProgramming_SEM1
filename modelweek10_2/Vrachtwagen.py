from .Voertuig import Voertuig

class Vrachtwagen(Voertuig):

    def __init__(self, id, merk, bouwjaar, kmstand, max_laadvermogen):
        super().__init__(id, merk, bouwjaar, kmstand)
        self.max_laadvermogen = max_laadvermogen
        self.vracht = 0 #volgorde is belangrijk

    # ********** property vracht - (setter/getter) ***********
    @property
    def vracht(self):
        """ The vracht property. """
        return self.__vracht
    
    @vracht.setter
    def vracht(self, value):
        if (type(value) is int or type(value) is float) and value < self.max_laadvermogen:
            self.__vracht = value   
        else:
            raise ValueError("Fout vracht")
    
    # ********** property max_laadvermogen - (setter/getter) ***********
    @property
    def max_laadvermogen(self):
        """ The max_laadvermogen property. """
        return self.__max_laadvermogen
    
    @max_laadvermogen.setter
    def max_laadvermogen(self, value):
        if type(value) is int or type(value) is float:
            self.__max_laadvermogen = value
        else: 
            raise ValueError("Fout max_laadvermogen")
    
    def __str__(self):
        return f"Vrachtwagen: {self.merk} {self.bouwjaar}"

    def geef_detail_info(self):
        info = f"Detail info over vrachtwagen {self.merk} ({self.bouwjaar}):\n"
        info += f"\t- ID: {self.id}\n"
        info += f"\t- Reisbestemming: "
        if self.reisbestemming == "":
            info += f"Onbekend\n"
        else:
            info += f"{self.reisbestemming}\n"
        info += f"\t- Max laadvermogen: {self.max_laadvermogen}\n"
        info += f"\t- Gewicht vracht: {self.vracht}\n"
        return info

        #return f"\t- ID: {self.id}\n\t- Reisbestemming: {self.Reisbestemming}\n\t- Max laadvermogen: {self.max_laadvermogen}\n\t- Gewicht vracht: {self.vracht}"