# Oef 01
# Deel 1
# Werk verder op de demo uit de theorieles. (Zie ook bronmateriaal bij deze opgave)
# Voeg de klasse ‘Ouder’ toe die erft van de klasse Persoon.
# Deze klasse houdt één extra attribuut bij, nl. een list van studenten (we gaan er voor
# de eenvoud vanuit dat alle kinderen studenten zijn). In de init-methode zet je hiervoor
# een lege list klaar. In deze list komen dus objecten van de klasse Student.
# Let op met het gebruik vande juiste termen: de klasse Ouder erft van de klasse Persoon
# over. De klasse Ouder houdt een list van objecten van de klasse Student bij: tussen de
# klasses Ouder en Student is er dus een associatie aanwezig.
# Werk deze klasse nu systematisch uit. Test regelmatig (via de beschikbare testcode).
# • Implementeer de methodes __init__( ) & __str__( )
# • Een property-methode ‘studenten’ die de list van studenten teruggeeft.
# Een setter-methode hoeft niet toegevoegd te worden.
# • Een methode ‘voeg_student_toe’ langs waar een student kan toegevoegd
# worden. Controleer vooraf of de student nog niet in de list aanwezig is.
# Welke achterliggende methode uit de klasse Student wordt bij deze controle
# gebruikt?
# • Een methode ‘geef_info_studenten’ die een string teruggeeft waarin zowel de
# info van de ouder als de info over elke student verwerkt zit.
# • Een methode ‘geef_opleidingen_studenten’ die een list met de namen van de
# opleidingen van de kinderen teruggeeft. Dubbels mogen niet voorkomen.
# Test alle methodes uit.
# Persoon
# Student Docent Ouder
# Week 10
# Basic Programming (skills) / 4
# Maak finaal ook een nieuw object van de klasse Auto aan waarbij de ouder als
# eigenaar wordt ingesteld.
# Hoe verhoudt de klasse Persoon zich tov de klasse Auto?
# Print de __str__() van de klasse Auto af. Dient de klasse Auto aangepast te worden?
# Waarom wel/niet?
# Opmerking: Je kan de test-methode in het bronmateriaal van deze oefening gebruiken.
# Een voorbeeld kan er als volgt uitzien:

from modelweek10_1.Auto import Auto
from modelweek10_1.Student import Student
from modelweek10_1.Ouder import Ouder

# LABO
def test_ouder():

    student1 = Student("Spriet", "Nick", 199510548, "MCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "MIT", 1992)

    ouder1 = Ouder("Spriet","Marc",1951)
    ouder1.voeg_student_toe(student1)
    ouder1.voeg_student_toe(student2)
    ouder1.voeg_student_toe(student3)
    print(ouder1)

    print(ouder1.geef_info_studenten())
    print(f"De verschillende opleidingen van de kinderen zijn: {ouder1.geef_opleidingen_studenten()}")

    #bespreek onderstaande code mbv de verschillende klasses
    print("\nOuder wordt de eigenaar van een auto.\nDe info van de auto is:")
    auto1 = Auto("1-DVX-656", ouder1)
    print(auto1)

    print("\nOuder geeft auto door aan één van zijn kinderen.\nDe info van de auto is:")
    #eigenaar is een object van de klasse Persoon
    #de subklasses (student, docent, ouder) kunnen hier dus ook gebruikt worden
    auto1.eigenaar = student1
    print(auto1)

test_ouder()
