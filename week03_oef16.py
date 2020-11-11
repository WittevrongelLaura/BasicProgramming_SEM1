# Oef 16
# Maak een functie met als parameters minimum_lengte en maximum_lengte. De functie genereert een
# willekeurig paswoord bestaande uit een combinatie van kleine en hoofdletters, én waarvan de lengte
# van het genereerde paswoord tussen beide grenzen valt.
# Tip: maak gebruik van string.ascii_letters uit de klasse string
import random 
import string


aantal = random.randint(5, 10)
nieuw_paswoord = ""

for i in range(0, aantal):
    random_letter = random.choice(string.ascii_letters)
    nieuw_paswoord +=random_letter

print(nieuw_paswoord)