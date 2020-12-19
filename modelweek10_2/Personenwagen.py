from .Voertuig import Voertuig


class Personenwagen(Voertuig):

    def __init__(self, id, merk, bouwjaar, kmstand, max_aantal_zitplaatsen):
        super().__init__(id, merk, bouwjaar, kmstand)
        self.max_aantal_zitplaatsen = max_aantal_zitplaatsen
        self.__aantal_personen = 0

    # ********** property max_aantal_zitplaatsen - (setter/getter) ***********
    @property
    def max_aantal_zitplaatsen(self):
        """ The max_aantal_zitplaatsen property. """
        return self.__max_aantal_zitplaatsen

    @max_aantal_zitplaatsen.setter
    def max_aantal_zitplaatsen(self, value):
        if type(value) is int and value >= 0:
            self.__max_aantal_zitplaatsen = value
        else:
            raise ValueError("Fout max zitplaatsen")

    # ********** property aantal_personen - (setter/getter) ***********
    @property
    def aantal_personen(self):
        """ The aantal_personen property. """
        return self.__aantal_personen

    @aantal_personen.setter
    def aantal_personen(self, value):
        if type(value) is int and value <= self.max_aantal_zitplaatsen:
            self.__aantal_personen = value
        else:
            raise ValueError(
                "Fout: er kunnen niet meer personen in dan er zitplaatsen zijn")

    # ********** property vrije_plaatsen - (enkel getter) ***********
    # calculated propery ->  is een property ZONDER attribuut maar berkend op basis
    # van andere properties
    @property
    def vrije_plaatsen(self):
        """ The vrije_plaatsen property. """
        return self.max_aantal_zitplaatsen - self.aantal_personen

    def __str__(self):
        return f"Personenwagen: {self.merk} {self.bouwjaar}"

    def geef_detail_info(self):
        info = f"Detail info over personenwagen {self.merk} ({self.bouwjaar}):\n"
        info += f"\t- ID: {self.id}\n"
        info += f"\t- Reisbestemming: "
        if self.reisbestemming == "":
            info += f"Onbekend\n"
        else:
            info += f"{self.reisbestemming}\n"
        info += f"\t- Aantal zitplaatsen: {self.max_aantal_zitplaatsen}\n"
        info += f"\t- Aantal vrije plaatsen: {self.vrije_plaatsen}\n"
        return info
