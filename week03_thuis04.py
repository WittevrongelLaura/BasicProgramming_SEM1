# Thuis 4
# Schrijf de functie controleer_emailadres die controleert of het gaat om een geldig studenten emailadres
# (voornaam.naam@student.howest.be).
# Op wat kan je allemaal controleren?

def controleer_emailadres(email):
    #dot = email.find(".")
    at = email.find("@")

    if at > 0:
        print("@ gevonden")
        deel1 = email[:at]
        if deel1.find(".") > 0:
            print("dot gevonden")
            deel2 = email[at + 1:]
            if deel2 == "student.howest.be":
                print("geldig studenten emailadres")
            else:
                print("geen geldig studenten emailadres")
        else:
            print("dot niet gevonden")
    else:
        print("geen geldig emailadres")

email = "laura.wittevrongel@student.howest.be"
controleer_emailadres(email)