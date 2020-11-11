# Week 03
# Basic Programming (skills) / 5
# Oef 11
# Vraag aan de gebruiker twee jaartallen op. Print de schrikkeljaren tussen deze twee jaartallen af.
# Opmerking: maak eerst een functie ‘is_schrikkeljaar’ waarbij getest wordt of een jaartal al dan niet een
# schrikkeljaar is. https://www.am-pm.nl/schrikkeljaar/
# Roep dan deze functie op voor elk jaartal dat tussen de opgegeven grenzen ligt.
# Gebruik van String
# Oef 12
# Vraag aan de gebruiker een woord, print vervolgens elk karakter onder elkaar af.
# Oef 13
# Schrijf een functie ‘swap’ die twee strings binnenkrijgt. De functie stelt één nieuwe string op waarbij de
# twee letters van elk woord worden omgewisseld en beide nieuwe woorden door een spatie gescheiden
# worden.
# Het resultaat van de functie is de nieuwe string.
# Voorbeeld: “abc” en “xyz” à “xyc abz”
# Oef 14
# Vraag aan de gebruiker zijn naam, voornaam en geboortedatum (formaat: dd-mm-yyyy) op. Genereer
# hiermee een paswoord door:
# - de eerste 3 karakters van de ingegeven familienaam (in kleine letters en zonder de eventuele
# spaties mee te nemen)
# - de eerste 2 karakters van de voornaam (in hoofdletters en ook zonder spaties)
# - 4 cijfers (mmyy) uit de geboortedatum.
# Maak hiervoor een afzonderlijke functie ‘genereer_paswoord’. Welke parameters gebruik je, wat zal de
# return waarde zijn?
# Voorbeeld:
# Oef 15
# Vraag aan de gebruiker zijn/haar howest-e-mailadres op. Haal hieruit de naam & voornaam en print
# deze af. Voor de eenvoud gaan we ervan uit dat de voornaam uit één deel bestaat. Zorg ervoor dat de
# eerste letter van de naam & voornaam met een hoofdletter afgeprint wordt.
# Week 03
# Basic Programming (skills) / 6
# Geef een correct howest-emailadres op:> stijn.walcarius@howest.be
# De familienaam is Walcarius en de voornaam is Stijn.
# Geef een correct howest-emailadres op:> charlotte.de.haene@howest.be
# De voornaam is Charlotte
# De naam is De Haene

email = "laura.wittevrongel@student.howest.be"

dot = email.find(".")
at = email.find("@")

voornaam = email[0:dot].capitalize()
naam = email[dot+1:at].capitalize()

print(voornaam)
print(naam)