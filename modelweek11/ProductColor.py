import logging

class ProductColor:

    def __init__(self, parcolorname, parhexvalue):
        self.colorname = parcolorname
        self.hexvalue = parhexvalue

    @property
    def hexvalue(self):
        """The hexvalue property."""
        return self.__hexvalue
    @hexvalue.setter
    def hexvalue(self, value):
        if value != "":
            self.__hexvalue = value
        else:
            logging.error(f"De hexvalue {value} is niet geldig")
            raise ValueError("Invalid hexvalue")
    
    @property
    def colorname(self):
        """The colorname property."""
        return self.__colorname
    @colorname.setter
    def colorname(self, value):
        if value != "":
            self.__colorname = value
        else:
            logging.error(f"De colorname {value} is niet geldig")
            raise ValueError("Invalid colorname")


    def __str__(self):
        return f"{self.colorname}"
    
    def __repr__(self):
        return f"{self.colorname}"
    
    def __eq__(self, other):
        if self.colorname == other.colorname and self.hexvalue == other.hexvalue:
            return True
        else:
            return False