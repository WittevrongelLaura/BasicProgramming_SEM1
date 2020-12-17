class Winkelkar:
    def __init__(self):
        self.__producten = [] #er is geen setter voorzien, dus rechtsstreeks

    @property
    def producten(self):
        """ The producten property. """
        return self.__producten
    
    
    def voeg_product_toe(self, nieuw_product):
        self.producten.append(nieuw_product)

    def verwijder_product(self, product_naam):
        if product_naam in self.producten:
            self.producten.remove(product_naam)

    def __str__(self):
        return f"De winkelkar bestaat uit {len(self.producten)}: {self.producten}"

