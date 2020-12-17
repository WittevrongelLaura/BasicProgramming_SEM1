# Oef 06
# Gegeven het bronbestand morse_vertaling.txt.
# Dit bronbestand staat in de submap ‘doc’ in. Analyseer het bronbestand: het bestaat uit een
# opsomming van letters met bijhorende morsevertaling. Merk op dat de eerste lijn van het
# bestand hier niet bijhoort. Wat zal je dus doen met de eerste lijn?
# Stap 1:
# Maak een applicatie die bestaat uit:
# • Dictionary ‘morse_dictionary’ (globale variabele)
# • Functie ‘inlezen_morse_bestand’:
# Die het morse-bestand correct inleest en de data in de dictionary bijhoudt (waarom?).
# o Hoe kan je de eerste lijn ‘overslaan’?
# • Print nadien de dictionary morse_dictionary af.
# • Functie ‘vertaal_letter’ met als parameter een letter (string). Deze functie controleert of
# de letter in de dictionary aanwezig is.
# o Indien zo wordt de vertaling teruggegeven, indien niet zo wordt een ‘?’ terug
# gegeven.

# Stap 2:
# Functie ‘vertaal_tekst_in_morse’ met als parameter een string (te_vertalen_tekst) die de
# doorgegeven tekst vertaalt en nadien de vertaling teruggeeft. Deze functie maakt gebruik van
# de net geschreven functie ‘vertaal_letter’.
# o Hoe kan je letter per letter vertalen? Welke structuur heb je hiervoor nodig?

# ENKEL MCT!
# Gebruik bestand in doc/morsevertaling.txt
dict_morse = {}


def inlezen_morse_bestand(bestandsnaam):
    dict_return = {}
    fo = open(bestandsnaam)
    lijn = fo.readline().rstrip("\n")
    #de eerste lijn overslaan
    lijn = fo.readline().rstrip("\n")
    while lijn != "":
        # verwerken van 1 lijn
        delen_lijn = lijn.split(";")
        #alpha = delen_lijn[0]
        #morse = delen_lijn[1]
        
        dict_return[delen_lijn[0]] = delen_lijn[1]
        lijn = fo.readline().rstrip("\n")
    fo.close()

    return dict_return

def vertaal_letter(letter):
    if letter in dict_morse.keys():
        return dict_morse[letter] 
    else:
        return "?"

def vertaal_woord(woord):
    vertaling_morse = ""
    for letter in woord:
        vertaling_morse += vertaal_letter(letter)
    return vertaling_morse

dict_morse = inlezen_morse_bestand('docweek06/morse_vertaling.txt')
print(f"MorseDictionary: {inlezen_morse_bestand('docweek06/morse_vertaling.txt')}")

letter = input("Geef een karakter (letter) in > ")
print(vertaal_letter(letter))

woord = input("Welk woord wil je vertalen? > ")
print(vertaal_woord(woord))
