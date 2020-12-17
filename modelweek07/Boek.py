class Boek:
    #init-methode (constructor)
    # object aanmaken
    def __init__(self, partitel, parauteur, paruitgeverij, parisbn, parjaargang=2020):
        self.__titel = partitel
        self.__auteur = parauteur
        self.__uitgeverij = paruitgeverij
        self.__isbn = parisbn
        self.__jaargang = parjaargang

    # properties (eigenschappen) -> zie opgave

    @property
    def titel(self):
        """ The titel property. """
        return self.__titel

    @titel.setter
    def titel(self, value):
        if value != "":
            self.__titel = value
        else:
            self.__titel = "onbekend"

    @property
    def auteur(self):
        """ The auteur property. """
        return self.__auteur

    @auteur.setter
    def auteur(self, value):
        if value != "":
            self.__auteur = value
        else:
            self.__auteur = "anoniem"

    @property
    def uitgeverij(self):
        """ The uitgeverij property. """
        return self.__uitgeverij

    @uitgeverij.setter
    def uitgeverij(self, value):
        if value != "":
            self.__uitgeverij = value
        else:
            self.__uitgeverij = "onbekend"

    @property
    def isbn(self):
        """ The isbn property. """
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        if value != "":
            self.__isbn = value
        else:
            self.__isbn = "onbekend"

    @property
    def jaargang(self):
        """ The jaargang property. """
        return self.__jaargang

    @jaargang.setter
    def jaargang(self, value):
        if type(value) is int and value >= 1900:
            self.__jaargang = value
        else:
            self.__jaargang = -1

    # toString-methode --> geeft string met info terug
    # object afprinten

    def __str__(self):
        return f"{self.auteur}, {self.titel} ({self.uitgeverij}) *{self.jaargang}*"
