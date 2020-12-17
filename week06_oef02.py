# Oef 02
# Maak een applicatie die controleert of een bestand ‘temp.txt’ wel of niet bestaat.
# Wanneer het bestand bestaat, dan wordt de functie ‘lees_bestand_in’ uit de vorige oefening
# aangeroepen.
# Wanneer het bestand nog niet bestaat, wordt de functie ‘schrijf_input_naar_bestand’
# aangeroepen.
# Deze functie maakt een nieuw bestand aan (met de bestandsnaam als parameter). Vervolgens
# vragen we meermaals aan de gebruiker om een lijn op te geven. Elke nieuwe lijn wordt
# onmiddellijk naar het bestand weggeschreven.
# Geef een nieuwe regel op, of druk op enter om te eindigen:> dit is een test
# Geef een nieuwe regel op, of druk op enter om te eindigen:> om meerdere lijnen
# Geef een nieuwe regel op, of druk op enter om te eindigen:> naar een bestand op te slaan
# Geef een nieuwe regel op, of druk op enter om te eindigen:>
# Press any key to continue . . .

import os

# MCT/ MIT
# Schrijf een tekst weg naar temp.txt

def lees_bestand_in(naam_bestand):
    fo = open(naam_bestand)

    #1e lees een lijn \n haalt enter uit einde uit de tekst
    line = fo.readline().rstrip("\n") 
    
    regelnr = 1
    while line != "":
        print(f"Regel {regelnr}: {line}")
        #volgende lijn lezen
        line = fo.readline().rstrip("\n")
        regelnr += 1
    fo.close()

def schrijf_input_naar_bestand(naam_bestand):
    fo = open(naam_bestand, "w")
    tekst = input("Geef een nieuwe regel of druk op enter > ")
    while tekst != "":
        fo.write(f"{tekst}\n")
        tekst = input("Geef een nieuwe regel of druk op enter > ")
    fo.close()

# vragen aan os of het bestand al bestaat
if os.path.exists("docweek06/temp.txt"):
    lees_bestand_in("docweek06/temp.txt")
else:
    schrijf_input_naar_bestand("docweek06/temp.txt")