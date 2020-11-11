# Oef 11
# Vraag aan de gebruiker twee jaartallen op. Print de schrikkeljaren tussen deze twee jaartallen af.
# Opmerking: maak eerst een functie ‘is_schrikkeljaar’ waarbij getest wordt of een jaartal al dan niet een
# schrikkeljaar is. https://www.am-pm.nl/schrikkeljaar/
# Roep dan deze functie op voor elk jaartal dat tussen de opgegeven grenzen ligt.

def is_schrikkeljaar(jaartal):
    if jaartal %4 == 0 and jaartal %100 != 0:
        return True
    elif jaartal %100 == 0 and jaartal %400 == 0:
        return True
    else:
        return False

jaartal1 = int(input("Geef een eerste jaartal in > "))
jaartal2 = int(input("Geef een tweede jaartal in > "))

for jaartal in range(jaartal1, jaartal2):
    if is_schrikkeljaar(jaartal):
        print(jaartal)