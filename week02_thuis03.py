# Thuis 3
# Schrijf een functie toon_boodschap die - afhankelijk van de het uur - volgende boodschap teruggeeft.
# Voorwaarde Resultaat
# Tussen 7.00 u en 11.59 u , dus uur is >=7 en <12 “Goede morgen, Karel”
# Tussen 12.00 u en 12.59 u , dus uur is …. “Joepie het is middag, Karel”
# Tussen 13.00 u en 16.59 u “Karel, goede namiddag”
# Tussen 17.00 u en 20.59 u “Karel, goede avond”
# Tussen 21.00 u en 6.59 u “Slaapwel Karel”
# Week 02
# Basic Programming (skills) / 7
# Je zal de functie als volgt oproepen. Vervolledig de code door zelf de functie toon_boodschap te
# schrijven.
# uur = int(input("Hoe laat is?"))
# voornaam = input("Wat is je voornaam?")
# verwelkoming = toon_boodschap(uur, voornaam)
# print(verwelkoming)
# Het resultaat zal het volgende zijn.
# Hoe laat is? 15
# Wat is je voornaam? Sarah
# Sarah, goede namiddag

def toon_boodschap(uur, naam):
    if uur >= 7 and uur < 12:
        return f"Goede morgen {naam}"
    elif uur >= 12 and uur < 13:
        return f"Joepie het is middag, {naam}"
    elif uur >= 13 and uur < 17:
        return f"{naam}, goede namiddag"
    elif uur >= 17 and uur < 21:
        return f"{naam}, goede avond"
    elif uur >= 21 and uur < 24:
        return f"Slaapwel, {naam}"
    elif uur >= 0 and uur < 7:
        return f"Slaapwel,{naam}"
    else:
        return "andere planeet"

uur = int(input("Hoe laat is het? > "))
voornaam = input("Wat is je voornaam? > ")
print(toon_boodschap(uur, voornaam))