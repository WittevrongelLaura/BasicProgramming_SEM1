class Hotelgast:
    # contructor (init)
    def __init__(self, parnaam, parvoornaam, parsaldo=0, paris_ingecheckt=True):
        self.naam = parnaam
        self.voornaam = parvoornaam
        self.saldo = parsaldo
        self.is_ingecheckt = paris_ingecheckt

    # properties
    # ****** property naam **********
    @property
    def naam(self):
        """ The naam property. """
        return self.__naam  # <--- ophalen van het private attribuut

    @naam.setter
    def naam(self, value):
        if value != "":
            self.__naam = value  # <--- opslaan van de value in het private attribuut
        else:
            self.__naam = "onbekend"

    # ******** property voornaam  *********
    @property
    def voornaam(self):
        """ The voornaam property. """
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        if value != "":
            self.__voornaam = value
        else:
            self.__voornaam = "onbekend"

    # ******** property saldo ************
    @property
    def saldo(self):
        """ The saldo property. """
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if type(value) is int and value >= 0:
            self.__saldo = value
        else:
            self.__saldo = 0

    # ********* property is_incheckt *********
    @property
    def is_ingecheckt(self):
        """ The is_ingecheckt property. """
        return self.__is_ingecheckt

    @is_ingecheckt.setter
    def is_ingecheckt(self, value):
        if type(value) is bool:
            self.__is_ingecheckt = value
        else:
            self.__is_ingecheckt = False

    # toString (str)
    def __str__(self):
        if self.is_ingecheckt is True:
            return f"OK {self.naam.upper()} - {self.saldo} euro"
        else:
            return f"X {self.voornaam} {self.naam}"

    def __eq__(self, other):
        if self.naam == other.naam and self.voornaam == other.voornaam:
            return True
        else:
            return False