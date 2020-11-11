# Oef 08
# Schrijf een functie print_welkom die een string als parameter heeft. Deze string stelt de naam voor.
# Print in de functie een welkomsbericht af waarin de naam gebruikt wordt. Deze functie zal dus geen
# returnwaarde hebben.
# Test de methode met verschillende namen.
# Wat is je voornaam? Sarah
# Welkom Sarah

def print_welkom(naam):
    print(f"Welkom {naam}")

voornaam = input("Wat is je voornaam? > ")
print_welkom(voornaam)