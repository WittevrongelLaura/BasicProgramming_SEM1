# Oef 03
# Maak de functie ‘vul_bestand_aan’. Deze functie is analoog aan de vorige functie
# ‘schrijf_input_naar_bestand’ behalve dat het bestand onderaan verder aangevuld wordt (en de
# bestaande inhoud dus niet gewist wordt). Test uit.
# Geef een nieuwe regel op, of druk op enter om te eindigen:> Nog een extra lijn
# Geef een nieuwe regel op, of druk op enter om te eindigen:> Om het af te leren
# Geef een nieuwe regel op, of druk op enter om te eindigen:> the end
# Press any key to continue . . .

# MCT/ MIT
# Voeg tekst toe aan temp.txt indien deze bestaat
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

def vul_bestand_aan(naam_bestand):
    fo = open(naam_bestand, "a")
    tekst = input("Geef een nieuwe regel of druk op enter > ")
    while tekst != "":
        fo.write(f"{tekst}\n")
        tekst = input("Geef een nieuwe regel of druk op enter > ")
    fo.close()

# # vragen aan os of het bestand al bestaat
# if os.path.exists("doc/temp.txt"):
#     lees_bestand_in("doc/temp.txt")
# else:
vul_bestand_aan("docweek06/temp.txt")