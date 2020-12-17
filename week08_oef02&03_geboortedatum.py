# Oef 02
# Maak een dataklasse Geboortedatum. Zorg ervoor dat dag, maand en jaar bijgehouden worden.
# Voorzie nu zelf de klasse van:
# • Voorzie de klasse van de nodige (eventueel) private attributen: dag, maand, jaar
# • Maak voor elk attribuut een (eventueel) publieke property aan.
# Bouw controles in wanneer dag/maand/jaar gewijzigd worden.
# o Tussen welke waarde moet een dag/maand liggen?
# • Programmeer de methode __init__()
# o Met 3 parameters dag, maand, jaar
# • Programmeer de methode __str__()
# o Met volgende output “dag/maand/jaar”
# Test de klasse uit!
# Breid de klasse vervolgens uit zodat het aantal gecreërde objecten van de klasse Geboortedatum
# bijgehouden wordt.
# • Maak hiervoor bovenaan een private static variabele __aantal_geboortedata aan.
# • Maak een public static methode ‘geef_aantal_geboortedatums’ om deze property op te
# vragen.
# Test de klasse uit!
# Breid de klasse uit met methodes die één random geboortedatum teruggeeft.
# • Maak een public static methode ‘genereer_willekeurige_verjaardag’
# • Maak een public static methode ‘genereer_lijst_verjaardagen’ die een list van willekeurige
# geboortedatums teruggeeft. De parameter is het gewenste aantal.
# Test elke nieuwe methode uit!
# Tot slot:
# • Integreer de methode __eq__() die instaat om de gelijkheid tussen twee geboortedatums
# te controleren. Bepaal eerst vooraf wanneer twee geboortedatums aan elkaar gelijk zijn.
# • Wat merk je op als je een list met Geboortedata afprint? De __str__() methode werkt niet
# in deze situatie? Welke methode moet je hiervoor voorzien?
# • Maak een (gewone) methode zelfde_verjaardag() met als parameter een object
# Geboortedatum, die controleert of beide op dezelfde dag verjaren (m.a.w. dag & maand
# zijn gelijk). Welk datatype kies als return waarde?
# • Test uit door verschillende objecten van deze klasse aan te maken en te vergelijken met
# elkaar.
# Week 08
# Basic Programming (skills) / 8
# Test klasse
# from model.Geboortedatum import Geboortedatum
# # controle
# datum1 = Geboortedatum(25, 9, 1977)
# print(datum1)
# datum1.dag = 32 # controle testen
# print(datum1)
# datum2 = Geboortedatum(25, 9, 1977)
# if (datum1 == datum2):
# print("gelijk")
# else:
# print("niet gelijk")
# print("Willekeurige lijst geboortedatums: ")
# aantal = int(input("Hoeveel geboortedatums wenst u? "))
# geboortedatums = Geboortedatum.genereer_lijst_geboortedata(aantal)
# index = 1
# for datum in geboortedatums:
# print(f"{index} : {datum} ")
# index += 1
# print(
# f"Totaal gecreëerde objecten van de klasse Geboortedatum:
# {Geboortedatum.geef_aantal_geboortedatums()}")
# Terminal
# 25/9/1977
# -1/9/1977
# niet gelijk
# Willekeurige lijst geboortedatums:
# Hoeveel geboortedatums wenst u? 3
# 1 : 19/2/2012
# 2 : 5/2/1953
# 3 : 18/5/1978
# Totaal gecreëerde objecten van de klasse Geboortedatum: 5

# Oef 03
# We integreren vorige oefeningen in elkaar. Zorg ervoor dat van elke speler ook de geboortedatum
# (object van de klasse Geboortedatum) wordt bijgehouden.
# • Maak een property geboortedatum (en bijhorend attribuut) in de klasse Speler aan.
# • Breid de constructor uit met een extra (optionele) parameter. Geef deze parameter een
# default-value, nl. 1 jan 2019
# Print van elke aangemaakte speler nu ook zijn geboortedatum af.
# Test klasse
# from models.Speler import Speler
# def test_spelers_oef3():
# sp1 = Speler("Thibault", "Cortous", "keeper", 8, 0, Geboortedatum(11,5,1992))
# sp2 = Speler("Vincent", "Kompany", "aanvaller", 8 ,3, Geboortedatum(10,4,1986))
# sp3 = Speler("Axel", "Witsel","aanvaller")
# print("De geboortedata van de spelers zijn:")
# for item in [sp1, sp2, sp3]:
# print(f"{item} -> gebootedatum: {item.geboortedatum}")
# test_spelers_oef3()
# Terminal
# De geboortedata van de spelers zijn:
# speler: Cortous, Thibault (8/10) doelpunten: 0 -> gebootedatum: 11/5/1992
# speler: Kompany, Vincent (8/10) doelpunten: 3 -> gebootedatum: 10/4/1986
# speler: Witsel, Axel (0/10) doelpunten: 0 -> gebootedatum: 1/1/2019


from modelweek08.Geboortedatum import Geboortedatum

def test_geboortedatums():
    # controle
    datum1 = Geboortedatum(25, 9, 1977)
    datum2 = Geboortedatum(19,2,1998)
    print(datum1)
    #aantal objecten aangemaakt
    print(Geboortedatum.geef_aantal_geboortedatums())

    nieuw = Geboortedatum.genereer_willekeurige_verjaardag()
    print(nieuw)
    # datum1.dag = 32  # controle testen
    # print(datum1)

    datum2 = Geboortedatum(25,9,1977)
    if (datum1 == datum2):
        print("gelijk")
    else:
        print("niet gelijk")

    
    print("Willekeurige lijst geboortedatums: ")
    aantal = int(input("Hoeveel geboortedatums wenst u? "))
    geboortedatums = Geboortedatum.genereer_lijst_verjaardagen(aantal)
    index = 1
    for datum in geboortedatums:
        print(f"{index} : {datum} ")
        index += 1

    lijst = [datum1, datum2]
    print(lijst)
    print(
        f"Totaal gecreëerde objecten van de klasse Geboortedatum: {Geboortedatum.geef_aantal_geboortedatums()}")


test_geboortedatums()

def deel2():
    datum1 = Geboortedatum(25, 9, 1977)
    datum2 = Geboortedatum(25,9,1998)
    if datum1.zelfde_verjaardag(datum2):
        print("deze mensen verjaren op dezelfde dag")

deel2()