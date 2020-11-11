# Thuis 1
# Gebruik jouw kassa-oplossing van vorige week.
# *** welkom bij het kassa systeem ***
# Hoeveel broeken werden er gekocht? 2
# Hoeveel T-shirts werden er gekocht? 3
# Hoeveel vesten werden er gekocht? 4
# Totaal te betalen:
# 604.87
# Verplaatst nu de berekening in een functie Kassa dat het kassasysteem nabootst. De functie geeft terug
# wat het totaal te betalen bedrag is.
# - Wat zijn de parameters van deze functie? Maw welke waarden veranderen binnen de berekening?
# - Wat geeft deze functie terug? Datatype?
# - Zorg dat je binnen de functie geef input of print gebruikt!
# Test uit!

def kassa(aantal_broeken, aantal_tshirten, aantal_vesten):
    totaal_broeken = aantal_broeken * broek
    totaal_tshirten = aantal_tshirten * tshirt
    totaal_vesten = aantal_vesten * vest
    totaal = totaal_broeken + totaal_tshirten + totaal_vesten
    return totaal

broek = 70.5
tshirt = 20.89
vest = 100.3
print("*** welkom bij het kassa systeem ***")
num_broek = int(input("Hoeveel broeken werden er gekocht? > "))
num_shirt = int(input("Hoeveel t-shirts werden er gekocht? > "))
num_vest = int(input("Hoeveel vesten werden er gekocht? > "))

#totaal = prijs_broek + prijs_tshirt + prijs_vest

print(f"Totaal te betalen: {kassa(num_broek, num_shirt, num_vest)}")