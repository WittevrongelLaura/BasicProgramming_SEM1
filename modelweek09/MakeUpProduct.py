from .ProductColor import ProductColor


class MakeUpProduct:
    # constructor
    def __init__(self, parid, parbrand, parname, parprice, parproductlink):
        self.id = parid
        self.brand = parbrand
        self.name = parname
        self.price = parprice
        self.productlink = parproductlink
        self.__colors = []

    # properties
    # ********** property id - (setter/getter) ***********

    @property
    def id(self):
        """ The id property. """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    # ********** property brand - (setter/getter) ***********
    @property
    def brand(self):
        """ The brand property. """
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    # ********** property name - (setter/getter) ***********
    @property
    def name(self):
        """ The name property. """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # ********** property price - (setter/getter) ***********
    @property
    def price(self):
        """ The price property. """
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    # ********** property productlink - (setter/getter) ***********
    @property
    def productlink(self):
        """ The productlink property. """
        return self.__productlink

    @productlink.setter
    def productlink(self, value):
        self.__productlink = value

    # ********** property colors - (setter/getter) ***********
    @property
    def colors(self):
        """ The colors property. """
        return self.__colors

    # toString
    def __str__(self):
        return f"{self.name} ({self.brand}) -> Available Colors: {len(self.colors)}"

    def __repr__(self):
        return f"{self.name}"

    # Extra functies
    def add_productcolor(self, new_color):
        if type(new_color) is ProductColor and new_color not in self.colors:
            self.__colors.append(new_color)
        else:
            print("foutkleur")

    def __lt__(self, other):
        if len(self.colors) < len(other.colors):
            return True
        else:
            return False