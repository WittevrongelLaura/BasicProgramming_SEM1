# Oef 02
# Maak een lege list ‘nieuwe_list_getalllen’ aan. Vul deze list op met getallen startend vanaf 1, met
# stapgrootte 13, tem 482. Doe nu het volgende:
# - Print de list af.
# - Print de list in omgekeerde volgorde af.
# - Verwijder het eerste element (waarde 482) en print opnieuw de list af.
# - Zoek de werkwijze om een specifiek element uit de list te verwijderen.

nieuwe_list = []

for getal in range(1, 482+1, 13):
    nieuwe_list.append(getal)

print(nieuwe_list)

nieuwe_list.reverse()
print(nieuwe_list)

del(nieuwe_list[0])
print(nieuwe_list)

nieuwe_list.remove(66)
print(nieuwe_list)