# Thuis 2
# Schrijf een programma dat een kassasysteem nabootst.
# • Een broek kost 70,5 euro.
# • Een T-shirt kost 20,89 euro.
# • Een vest kost 100,3 euro.
# De gebruiker geeft per item het aantal gekochte goederen in. De computer berekent het te betalen
# bedrag.
# *** welkom bij het kassa systeem ***
# Hoeveel broeken werden er gekocht? 2
# Hoeveel T-shirts werden er gekocht? 3
# Hoeveel vesten werden er gekocht? 4
# Totaal te betalen:
# 604.87

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

print(f"Totaal te betalen: {prijs_broek + prijs_tshirt + prijs_vest}")