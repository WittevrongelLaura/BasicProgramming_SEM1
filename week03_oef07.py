# Oef 07
# Vraag aan de gebruiker volgende 3 getallen op:
# - een startwaarde
# - een positieve stapgrootte
# - het gewenste aantal af te printen getallen
# Schrijf een functie ‘print_lijst_getallen’ die deze 3 getallen als parameter binnen krijgt. De functie print
# een lijst, met het gewenste aantal getallen, af waarbij het eerste getal gelijk is aan de startwaarde en de
# getallen met de stapgrootte vergroten.De functie heeft geen return waarde. Het afprinten gebeurt IN de
# functie.

start = int(input("Geef een startwaarde op > "))
stap = int(input("Geef een positieve startgrootte op > "))
aantal = int(input("Hoeveel getallen moeten er afgeprint worden? > "))

def print_lijst_getallen(start, stap, aantal_getallen):
    print("De lijst met getallen is:")
    stop = start + (stap * aantal_getallen)
    for getal in range(start, stop, stap):
        print(getal)

print_lijst_getallen(start, stap, aantal)