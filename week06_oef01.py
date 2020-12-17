# Oef 01
# Voeg een tekstbestand toe aan uw projectmap. Voorzie het tekstbestand van verschillende
# regels tekst. Maak nu een functie ‘lees_bestand_in’ die het tekstbestand inleest en lijn per lijn
# afprint. De parameter van de functie is de bestandsnaam. Elke lijn wordt door een lijnnummer
# vooraf gegaan.
# Voorbeeld:
# Inhoud bestand:
# Regel 1: Dit is een test
# Regel 2: om meerdere lijnen
# Regel 3: na elkaar
# Regel 4: in te lezen.

# MCT/ MIT
# Gebruik bestand in doc/intelezen.txt

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


lees_bestand_in("docweek06/intelezen.txt")