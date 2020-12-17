# Oef 03
# Maak een dataklasse Hotelgast en testklasse test_hotelgast. Van een hotelgast
# bewaar je in de (private) attributen
# • de naam
# • de voornaam
# • het openstaand saldo
# • of de gast al dan niet is ingecheckt (True/False)
# In de publiek setter property doe je volgende controle voordat je de waarde bewaart
# in de overeenkomstige attributen:
# • de naam mag niet leeg zijn, zoniet bewaar je ONBEKEND
# • de voornaam mag niet leeg zijn, zoniet bewaar je ONBEKEND
# • Het saldo moet een positief geheel getal zijn. Geeft de gebruiker een negatieve
# waarde in, dan wordt het saldo toch als 0 (euro) bewaard.
# • Je controleert of het type van is_ingecheckt een bool(ean) is.
# o Is het een ander gegevenstype, dan bewaar je de waarde False.
# Programmeer de constructor of de methode __init__()
# • De parameters zijn naam, voornaam, saldo en is_ingecheckt.
# Programmeer de methode __str__()
# • De output voor ingechekte personen is “OK: Familienaam – saldo euro”
# • De output voor uitgechekte personen is “X: Voornaam Familienaam”
# Controleer of de functionaliteit in orde is. Je kan hiervoor ook het testbestand op Leho
# gebruiken.
# from model.Hotelgast import Hotelgast
# gast1 = Hotelgast("Walcarius", "Stijn", -100, True)
# gast2 = Hotelgast("Roobrouck", "Dieter", 30, False)
# print("*** Volgende gasten verblijven bij ons: ")
# print(gast1)
# print(gast2)
# print("**** chekckt uit met fout")
# gast1.is_ingecheckt = "gaat weg"
# print(gast1)
# Terminal
# *** Volgende gasten verblijven bij ons:
# OK: WALCARIUS - 0 euro
# X: Dieter ROOBROUCK
# **** checkt uit met fout
# X: Stijn WALCARIUS


from modelweek07.Hotelgast import Hotelgast

gast1 = Hotelgast("Walcarius", "Stijn", -100, True)
gast2 = Hotelgast("Roobrouck", "Dieter", 30, False)

print("*** Volgende gasten verblijven bij ons: ")
print(gast1)
print(gast2)
print("**** checkt uit met fout")
gast1.is_ingecheckt = "gaat weg"
print(gast1) #wordt X door de controle in de setter