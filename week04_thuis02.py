# Thuis 2
# In een autoverhuurbedrijf worden dagelijks verschillende wagens verhuurd. De huurprijs bestaat uit een
# vast gedeelte aangevuld met een variabel gedeelte (kost per afgelegde km)
# Er zijn drie verschillende types wagens die men kan huren:
# - Voor wagens van het type A: vast gedeelte bedraagt 25€/dag; variabel bedraagt 0,5€ per km
# - Voor wagens van het type B: vast gedeelte bedraagt 35€/dag; variabel bedraagt 0,6€ per km
# - Voor wagens van het type C: vast gedeelte bedraagt 45€/dag; variabel bedraagt 0,7€ per km
# Jouw programma verzorgt de boekhouding van het autoverhuurbedrijf. Bij het terugbrengen van de auto
# geef je op:
# - Over welk type het gaat
# - Het aantal dagen dat de huurder de wagen benut heeft
# - Het aantal gereden kilometers
# Op het einde van de dag moeten volgende gegevens op het scherm getoond worden:
# • het totale bedrag aan inkomsten
# • het totale bedrag aan inkomsten van wagens van het type A,
# • het totale bedrag aan inkomsten van wagens van het type B,
# • het totale bedrag aan inkomsten van wagens van het type C,
# •
# • het totaal aantal wagens van het type A die verhuurd werden,
# • het totaal aantal wagens van het type B die verhuurd werden,
# • het totaal aantal wagens van het type C die verhuurd werden,
# •
# • het totaal aantal gereden km van de wagens van type A,
# • het totaal aantal gereden km van de wagens van type B,
# • het totaal aantal gereden km van de wagens van type C,

def prijs_per_dag(aantal_dagen, prijs):
    return aantal_dagen * prijs

def prijs_per_km(aantal_km, prijs_km):
    return aantal_km * prijs_km

a_vast = 25
a_variabel = 0.5
b_vast = 35
b_variabel = 0.6
c_vast = 45
c_variabel = 0.7

totaal_inkomen = []
inkomen_a = []
inkomen_b = []
inkomen_c = []
aantal_wagens_a = 0
aantal_wagens_b = 0
aantal_wagens_c = 0
aantal_km_a = 0
aantal_km_b = 0
aantal_km_c = 0


aantal_ingeleverde_wagens = int(
input("Hoeveel wagens werden er ingeleverd? > "))

for index in range(0, aantal_ingeleverde_wagens):
    type_wagen = input("Over welk type gaat het? (A, B of C) > ")
    aantal_dagen = int(input("Hoeveel dagen werd de wagen verhuurd? > "))
    aantal_gereden_km = int(input("Aantal gereden km: > "))
    if type_wagen.lower() == "a":
        inkomen_a.append(prijs_per_dag(aantal_dagen, a_vast) + prijs_per_km(aantal_gereden_km, a_variabel))
        aantal_wagens_a += 1
        aantal_km_a += aantal_gereden_km
    elif type_wagen.lower() == "b":
        inkomen_b.append(prijs_per_dag(aantal_dagen, b_vast) + prijs_per_km(aantal_gereden_km, b_variabel))
        aantal_wagens_b += 1
        aantal_km_b += aantal_gereden_km
    elif type_wagen.lower() == "c":
        inkomen_c.append(prijs_per_dag(aantal_dagen, c_vast) + prijs_per_km(aantal_gereden_km, c_variabel))
        aantal_wagens_c += 1
        aantal_km_c += aantal_gereden_km
    else:
        print("Kies uit A, B of C")


print(f"Totale inkomsten: {sum(inkomen_a) + sum(inkomen_b) + sum(inkomen_c)}")
print(f"Totale inkomsten type A: {sum(inkomen_a)}")
print(f"Totale inkomsten type B: {sum(inkomen_b)}")
print(f"Totale inkomsten type C: {sum(inkomen_c)}\n")

print(f"Aantal ingeleverde wagens type A: {aantal_wagens_a}")
print(f"Aantal ingeleverde wagens type B: {aantal_wagens_b}")
print(f"Aantal ingeleverde wagens type C: {aantal_wagens_c}")
print(
    f"Totaal aantal ingeleverde wagens: {aantal_wagens_a + aantal_wagens_b + aantal_wagens_c}\n")

print(f"Totaal aantal gereden km van type A wagens: {aantal_km_a}")
print(f"Totaal aantal gereden km van type B wagens: {aantal_km_b}")
print(f"Totaal aantal gereden km van type C wagens: {aantal_km_c}")
