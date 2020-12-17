# Thuis 1
# Maak een dataklasse Postpakket. Van een postpakket bewaar je volgende items:
# omschrijving, breedte, hoogte en diepte.
# • Voorzie de klasse van de nodige (private) attributen en bijhorende getter en setter
# property-methodes.
# • In de (publiek) setter property-methodes doe je volgende controle voordat je de
# waarde bewaart in de overeenkomstige attributen:
# o De breedte, hoogte en diepte moet een geheel getal zijn.
# o De breedte, hoogte en diepte moet groter zijn dan 0 (cm). Anders geef je het
# de waarde 1 (cm)
# • De omschrijving mag niet gewijzigd worden. Deze heeft enkel een (publieke)
# getter property-methode.
# o Tip: welk effect zal dit straks hebben binnen in de constructor __init()__?
# • Er is nog één extra getter property-methode die geen attribuut heeft.
# o Deze geeft het volume terug (breedte * hoogte * diepte)
# • Programmeer de methode __init__()
# o Heeft de volgende parameters omschrijving, breedte, hoogte en diepte
# • Programmeer de methode __str__()
# o Geeft volgende output:
# o Pakketje: omschrijving (breedte cm* hoogte cm* diepte cm)
# Test volgende code uit. Je kan hiervoor het testbestand op Leho gebruiken.
# from model.Postpakket import Postpakket
# bol = Postpakket("GSM", 3, 3, 4)
# print(bol)
# print(f"Volume van pakket is: {bol.volume:.2f}")
# amazon = Postpakket("Alexa",3.3,34,3)
# print(amazon)
# Terminal
# Pakketje: GSM (3 cm * 3 cm * 4 cm)
# Volume van pakket is: 36.00
# Pakketje: Alexa (1 cm * 34 cm * 3 cm)

from modelweek07.Postpakket import Postpakket

bol = Postpakket("GSM", 3, 3, 4)
print(bol)

print(f"Volume van pakket is: {bol.volume:.2f}")

amazon = Postpakket("Alexa", 3.3, 34, 3)
print(amazon)
