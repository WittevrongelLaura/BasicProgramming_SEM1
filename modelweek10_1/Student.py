from .Persoon import Persoon


class Student(Persoon):

    def __init__(self, parnaam, parvoornaam, parstudentennummer, paropleiding, pargeboortejaar=2019):
        # Persoon.__init__(self, parnaam, parvoornaam, pargeboortejaar)
        super().__init__(parnaam, parvoornaam, pargeboortejaar)
        self.studentennummer = parstudentennummer
        self.opleiding = paropleiding

    @property
    def studentennummer(self):
        return self.__studentennummer

    @studentennummer.setter
    def studentennummer(self, value):
        if type(value) is int:
            self.__studentennummer = value
        else:
            raise ValueError("Geen geldig studentennummer!")

    @property
    def opleiding(self):
        return self.__opleiding

    @opleiding.setter
    def opleiding(self, value):
        if value:
            self.__opleiding = value
        else:
            raise ValueError("Geen geldige opleiding!")

    def __str__(self):
        return f"Student {super().__str__()}"

    # niet nodig indien identiek met superklasse
    # def __repr__(self):
    #     return f"{super().__repr__()}"

    def __repr__(self):
        return f"Student {self.naam} {self.voornaam}"

    def __eq__(self, other):
        #print("eq - Student")
        if self.studentennummer == other.studentennummer:
            return True
        else:
            return False
