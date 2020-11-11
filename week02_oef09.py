# Oef 09
# Schrijf een functie maak_verwelkoming_klas die twee strings als parameters heeft: naam en klasgroep.
# Zorg dat de parameter groep een defaultwaarde ‘1MIT1’ krijgt.
# Print het welkomstbericht, waarin naam & klasgroep vermeld staan, buiten de functie. Deze functie
# heeft met andere woorden wel een returnwaarde.
# Het voordeel van deze werkwijze is dat je later kan beslissen wat je met de uitkomst van de functie
# doet. De functie werkt volledig autonoom van de in- of output. Deze werkwijze heeft de voorkeur.
# Test de functie voldoende (zowel met 1 als 2 argumenten)

def maak_verwelkoming_klas(naam, klasgroep = "1MIT1"):
    return f"welkom {naam} in de groep {klasgroep}"

print(maak_verwelkoming_klas("laura"))