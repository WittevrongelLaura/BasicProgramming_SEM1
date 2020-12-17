class Winkelkar:
    # constructor
    def __init__(self):
        self.__producten = []
        # er is geen setter voorzien, dus rechtstreeks op private attribuut

    # properties
    @property
    def producten(self):
        """ The producten property. """
        return self.__producten

    # toString
    def __str__(self):
        return f"De winkelkar bestaat uit {len(self.producten)} : {self.producten} "

    # extra functies
    def voeg_product_toe(self, nieuw_product):
        self.producten.append(nieuw_product)

    def verwijder_product(self, product_naam):
        if product_naam in self.producten:
            self.producten.remove(product_naam)

    #operator + programmeren
    def __add__(self, other):
        w = Winkelkar()
        for product in self.producten:
            w.voeg_product_toe(product)
        
        for product in other.producten:
            w.voeg_product_toe(product)

        return w

    # operator += programmeren -> producten uit other bij mij (self) gestoken
    def __iadd__(self, other):
        for product in other.producten:
            self.voeg_product_toe(product)
        #het resultaat ben ik zelf
        return self