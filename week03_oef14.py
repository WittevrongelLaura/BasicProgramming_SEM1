# Oef 14
# Vraag aan de gebruiker zijn naam, voornaam en geboortedatum (formaat: dd-mm-yyyy) op. Genereer
# hiermee een paswoord door:
# - de eerste 3 karakters van de ingegeven familienaam (in kleine letters en zonder de eventuele
# spaties mee te nemen)
# - de eerste 2 karakters van de voornaam (in hoofdletters en ook zonder spaties)
# - 4 cijfers (mmyy) uit de geboortedatum.
# Maak hiervoor een afzonderlijke functie ‘genereer_paswoord’. Welke parameters gebruik je, wat zal de
# return waarde zijn?


def genereer_paswoord(naam, voornaam, datum):
    deel_naam = naam.replace(" ", "")[:3].lower()
    deel_voornaam = voornaam[:2].upper()
    deel_datum = datum[3:5] + datum[8:]
    return f"{deel_naam + deel_voornaam + deel_datum}"

print(genereer_paswoord("wittevrongel", "laura", "19-02-1998"))