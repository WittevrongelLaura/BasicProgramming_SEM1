class ProductColor:
    # constructor
    def __init__(self, parcolorname, parhexvalue):
        self.colorname = parcolorname
        self.hexvalue = parhexvalue

    # properties
    # ********** property colorname - (setter/getter) ***********
    @property
    def colorname(self):
        """ The colorname property. """
        return self.__colorname
    
    @colorname.setter
    def colorname(self, value):
        if type(value) is str and value != "":
            self.__colorname = value
        else:
            raise ValueError("Geen geldige kleurnaam")

    # ********** property hexvalue - (setter/getter) ***********
    @property
    def hexvalue(self):
        """ The hexvalue property. """
        return self.__hexvalue
    
    @hexvalue.setter
    def hexvalue(self, value):
        self.__hexvalue = value
    
    
    
    # tosString
    def __str__(self):
        return f"{self.colorname}"
    # Extra functies
    def __repr__(self):
        return f"{self.colorname}"

    def __eq__(self, other):
        if self.hexvalue == other.hexvalue:
            return True
        else:
            return False