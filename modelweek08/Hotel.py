from .Hotelgast import Hotelgast

class Hotel:
    __lijst_gasten = []
    def __init__(self, parnaam):
        self.naam = parnaam
        self.__gasten = [] #er is geen setter, dus rechtstreeks op private attribuut

    # ********** property naam - (setter/getter) ***********
    @property
    def naam(self):
        """ The naam property. """
        return self.__naam
    
    @naam.setter
    def naam(self, value):
        self.__naam = value
    
    # ********** property gasten - (setter/getter) ***********
    @property
    def gasten(self):
        """ The gasten property. """
        return self.__gasten
    
    def __str__(self):
        return f"Hotel: {self.naam}"

    def check_in(self, naam, voornaam):
        nieuwe_gast = Hotelgast(naam, voornaam)
        if not nieuwe_gast in self.gasten:
            nieuwe_gast.is_ingecheckt = True
            self.__gasten.append(nieuwe_gast)
            print(f"Correct ingecheckt {nieuwe_gast}")
        else:
            print(f"De hotelgast {nieuwe_gast} is reeds ingecheckt")

    def print_info_gasten(self):
        print(f"Dit zijn de aanwezige gasten in hotel {self.naam}")
        for temp_gast in self.gasten:
            print(temp_gast)

    def __zoek_hotelgast(self, naam, voornaam):
        temp_gast = Hotelgast(naam, voornaam)
        for gast_in_lus in self.gasten:
            #overloop alle gasten (met alle properties)
            if gast_in_lus == temp_gast:
                return gast_in_lus#gast in lus bevat alle properties
        return None

    def check_out(self, naam, voornaam):
        gast = self.__zoek_hotelgast(naam, voornaam)
        if not gast is None:
            #gast is gevonden
            #controleer of de gast nog een saldo > 0 heeft
            if gast.saldo > 0:
                print(f"Gast {gast} heeft nog een openstaand saldo, ik kan hem niet uitchecken")
            else:
                #uitchecken
                self.gasten.remove(gast) #de gevonden gast, verwijder ik van de lijst
                print(f"{gast} is correct uitgecheckt")
        else:
            print(f"Gast {naam} {voornaam} niet gevonden")

    def bestel_drank(self, naam, voornaam, kostprijs):
        gast = self.__zoek_hotelgast(naam, voornaam)
        if not gast is None:
            gast.saldo += kostprijs
        else:
            print(f"Gast {naam} {voornaam} niet gevonden")

    def vereffen_saldo_gast(self, naam, voornaam):
        gast = self.__zoek_hotelgast(naam, voornaam)
        if not gast is None:
            gast.saldo = 0
        else:
            print(f"Gast {naam} {voornaam} niet gevonden")