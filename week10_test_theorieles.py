from modelweek10_1.Auto import Auto
from modelweek10_1.Student import Student
from modelweek10_1.Docent import Docent
from modelweek10_1.Persoon import Persoon


def test_student():
    student1 = Student("Spriet", "Nick", 199510548, "MCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "MIT", 1992)
    studenten = [student1, student2, student3]
    print(f"De studenten: {studenten}")

    # zal dit werken & waarom (niet)?
    studenten.sort()
    print(f"Gesorteerd: {studenten}")

    # welke eq-methode wordt hier gebruikt?
    if student1 == student2:
        print("Gelijk")
    else:
        print("Verschillend")

# test_student()


def test_controle():
    # DOEL: controleren of een variabele een object van een kasse is die erft van een basisklasse
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    # werkt wel
    if isinstance(student1, Persoon):
        print("Via isinstance testen of student1 een PERSOON is: OK")
    else:
        print("Via isinstance testen of student1 een PERSOON is: NOK")

    # type werkt NIET voor controle op basis klasse
    if type(student1) is Persoon:
        print("Via type testen of student1 een PERSOON is: OK")
    else:
        print("Via type testen of student1 een PERSOON is: NOK")

    # type werkt enkel voor de subklasse
    if type(student1) is Student:
        print("Via type testen of student1 een STUDENT is")

# test_controle()


def test_docent():
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent1.geeft_les_in("MCT")

    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)
    docent2.geeft_les_in("MCT")
    docent2.geeft_les_in("MIT")

    # welke methode wordt hier uitgevoerd?
    print(docent1)
    print(docent2)

    # welke eq-methode wordt hier gebruikt?
    if (docent1 == docent2):
        print("Gelijk")
    else:
        print("Verschillend")

# test_docent()


def werkt_dit():
    student1 = Student("Spriet", "Nick", 199510548, "NMCT", 1995)
    student2 = Student("Spriet", "Fien", 199510412, "DAE", 1994)
    student3 = Student("Spriet", "Marieke", 199212212, "NMCT", 1992)
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)

    # werkt dit?
    print(f"Vereninging: {Docent.vereniging}")
    print(f"Aantal personen: {Student.geef_aantal_personen()}")
    print()

    # wat gebeurt er hier?
    for p in [student1, student2, student3, docent1, docent2]:
        print(f"{p} is {p.leeftijd} jaren oud.")


# werkt_dit()


def test_auto():
    student1 = Student("Spriet", "Nick", 199510548, "MCT", 1995)
    docent1 = Docent("Walcarius", "Stijn", 1125234, 1977)
    docent2 = Docent("Laprudence", "Christophe", 1685854, 1980)

    auto1 = Auto("1-HOW-125", docent1)
    auto2 = Auto("1-SWC-123", docent2)
    auto3 = Auto("1-LAP-945", student1)

    print("Dit zijn de verschillende voertuigen met hun eigenaars: ")
    for auto in [auto1, auto2, auto3]:
        print(auto)


# test_auto()
