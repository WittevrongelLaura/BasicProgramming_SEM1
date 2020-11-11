# Oef 12
# Schrijf een functie vertaal_maandnummer_naar_str die een maandnummer binnenkrijgt als parameter.
# Controleer in de functie of het getal tussen 1 en 12 ligt. Geef nadien de corresponderende maand terug.
# Indien buiten het interval, geef je een foutboodschap terug. Test de functie met meerdere
# maandnummers.
# Nadien test je je functie door volgende input aan de gebruiker te vragen.
# Geef een maandnummer: 9
# De overeenkomstige maand is -> september
# Geef een maandnummer: 13
# De overeenkomstige maand is -> onbekende maand

def vertaal_maandnummer_naar_str(maandnr):
    if maandnr > 1 and maandnr <= 12:
        if maandnr == 1:
            return "januari"
        elif maandnr == 2:
            return "februari"
        elif maandnr == 3:
            return "maart"
        elif maandnr == 4:
            return "april"
        elif maandnr == 5:
            return "mei"
        elif maandnr == 6:
            return "juni"
        elif maandnr == 7:
            return "juli"
        elif maandnr == 8:
            return "augustus"
        elif maandnr == 9:
            return "september"
        elif maandnr == 10:
            return "oktober"
        elif maandnr == 11:
            return "november"
        elif maandnr == 12:
            return "december"
        else:
            return "Hoe kan dit"
    else:
        return "Geef een geldige maandnr in"

maandnummer = int(input("Geef een maandnummer in: > "))
print(f"De overeekomstige maand is -> {vertaal_maandnummer_naar_str(maandnummer)}")