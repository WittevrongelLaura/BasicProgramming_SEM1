# Oef 03
# Maak een lege list ‘vrienden’ aan.
# We laten de applicatie deze list dynamisch uitbreiden. Telkens wordt aan de gebruiker gevraagd om een
# nieuwe naam op te geven of een lege string. In dat laatste geval stopt de applicatie door de lijst met
# vrienden af te printen.

vrienden = []

vriend = input("Geef de naam van een vriend op (sluit af met enter): > ")

while vriend != "":
    vrienden.append(vriend)
    vriend = input("Geef de naam van een vriend op (sluit af met enter): > ")

print(vrienden)