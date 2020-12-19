from .ProductColor import ProductColor
import logging

class MakeUpProduct:

    def __init__(self, parid, parbrand, parname, parprice, parproductlink):
        self.id = parid
        self.brand = parbrand
        self.name = parname
        self.price = parprice
        self.productlink = parproductlink
        self.__colors = []

    @property
    def id(self):
        """The id property."""
        return self.__id

    @id.setter
    def id(self, value):
        if value != "":
            self.__id = value
        else:
            logging.error(f"Het id {value} is niet geldig")
            raise ValueError("Invalid id!")  

    @property
    def brand(self):
        """The brand property."""
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value != "":
            self.__brand = value
        else:
            logging.error(f"De brand {value} is niet geldig")
            raise ValueError("Invalid brand!")            

    @property
    def name(self):
        """The name property."""
        return self.__name

    @name.setter
    def name(self, value):
        if value != "":
            self.__name = value
        else:
            logging.error(f"De name {value} is niet geldig")
            raise ValueError("Invalid name!")           

    @property
    def productlink(self):
        """The productlink property."""
        return self.__productlink

    @productlink.setter
    def productlink(self, value):
        if value != "":
            self.__productlink = value
        else:
            logging.error(f"De productlink {value} is niet geldig")
            raise ValueError("Invalid productlink!")   

    @property
    def price(self):
        """The price property."""
        return self.__price

    @price.setter
    def price(self, value):
        if type(value) is float and value < 10.0:
            self.__price = value
        else:
            logging.error(f"De price {value} is te hoog")
            raise ValueError("Invalid price!")               

    @property
    def colors(self):
        """The colors property."""
        return self.__colors

    def add_productcolor(self, new_color):
        if type(new_color) is ProductColor and new_color not in self.__colors:
            self.__colors.append(new_color)

    def __str__(self):
        return f"{self.name} ({self.brand}) -> Available Colors: {len(self.colors)}"

    def __repr__(self):
        return f"{self.name} - {len(self.colors)}"

    #nodig om te kunnen sorteren van een list
    def __lt__(self,other):
        if len(self.colors) < len(other.colors):
            return True
        else:
            return False