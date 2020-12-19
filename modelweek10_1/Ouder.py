# maak zelf de klasse ouder aan
from .Persoon import Persoon
from .Student import Student

class Ouder(Persoon):
    
    def __init__(self, par_naam, par_voornaam, par_geboortejaar=2020):
        #de init-methode van de basisklasse gaan aanroepen
        super().__init__(par_naam, par_voornaam, par_geboortejaar)
        #nieuwe (extra) zaken die enkel bij de klasse ouder horen
        self.__studenten = []

    #properties
    # ********** property studenten - (enkel getter) ***********
    @property
    def studenten(self):
        """ The studenten property. """
        return self.__studenten
    
    
    def __str__(self):
        #tostring methode gebruiken van de basisklasse
        return f"Ouder {super().__str__()} ({self.geboortejaar})"


    #extra methodes
    def voeg_student_toe(self, nieuwe_student):
        #controleer of nieuwe_student een object is van de klasse student
        if type(nieuwe_student) is not Student:
            raise ValueError("Geen geldige student.")
        elif nieuwe_student in self.__studenten:
            raise ValueError("Student is reeds eerder toegevoegd.")
        else:
            self.__studenten.append(nieuwe_student)
    
    #info (string) teruggeven met info over alle studenten & ouder
    def geef_info_studenten(self):
        info = f"{self} heeft de volgende studenten:\n"
        
        for student in self.__studenten:
            #to string van klasse student
            info += f"{student} volgt de opleiding {student.opleiding}\n"

        return info

    #geef in een list alle opleidingen van de studenten terug
    def geef_opleidingen_studenten(self):
        opleidingen = []
        #overloop al je studenten
        for student in self.__studenten:
            #zorg ervoor dat er geen dubbels inzitten
            if not student.opleiding in opleidingen:
                opleidingen.append(student.opleiding)

        return opleidingen