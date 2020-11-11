# Pas de uitvoer als volgt aan (let op het inspringen en de spaties):
# *** welkom bij het kassa systeem ***
# Hoeveel broeken werden er gekocht? 2
# Hoeveel T-shirts werden er gekocht? 3
# Hoeveel vesten werden er gekocht? 4
# U kocht:
# Broeken: 2 stuk(s)
# T-Shirts: 3 stuk(s)
# Vesten: 4 stuk(s)
# Totaal:604.87

broek = 70.5
tshirt = 20.89
vest = 100.3
print("*** welkom bij het kassa systeem ***")
num_broek = int(input("Hoeveel broeken werden er gekocht? > "))
num_shirt = int(input("Hoeveel t-shirts werden er gekocht? > "))
num_vest = int(input("Hoeveel vesten werden er gekocht? > "))

prijs_broek = broek * num_broek
prijs_tshirt = tshirt * num_shirt
prijs_vest = vest * num_vest

#totaal = prijs_broek + prijs_tshirt + prijs_vest
print(f"U kocht: \n\t"+
f"Broeken: {num_broek} stuk(s)\n\t"+
f"T-shirts: {num_shirt} stuk(s)\n\t"+
f"vesten: {num_vest} stuk(s)")
print(f"Totaal te betalen: {prijs_broek + prijs_tshirt + prijs_vest}")