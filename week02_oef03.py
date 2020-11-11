# Oef 03
# Vraag aan de gebruiker wat zijn geboortejaar is. Indien hij nog geen 18 is, print dan ook een gepaste
# melding af.
# (Tip: via module datetime kan je now-functionaliteit gebruiken. Gebruik hiervan het jaartal)
# (Extra: hou ook rekening met de geboortemaand en geboortedag om te verifiëren of iemand al 18 is.)
from datetime import datetime

geboortejaar = int(input("Wat is uw geboortejaar? > "))
geboortemaand = int(input("Wat is uw geboortemaand? > "))

huidig_jaar = datetime.now().year
huidige_maand = datetime.now().month

leeftijd = huidig_jaar - geboortejaar

if leeftijd < 18:
    print("U bent nog geen 18!")
elif leeftijd == 18:
    if geboortemaand < huidige_maand:
        #je bent jarig geweest
        print("Ok, u mag alcohol drinken")
    else:
        print("u bent nog geen 18!")
else:
    print("Ok, u mag alcohol drinken")