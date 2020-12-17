# Oef 01
# Je vertrekt van het startbestand Speler.py. Overloop de code: ga na welke properties/dataattributen
# aanwezig zijn.
# Breid de klasse uit:
# • de methode “maak_doelpunt” verhoogt het aantal eigen doelpunten van een speler
# • de methode “?????????????” zodat een speler correct wordt afgeprint binnen een list. Als
# een list van spelers wordt afgeprint
# • de ploegnaam wordt gedeeld over de volledige ploeg (public static variabele)
# • de doelpunten van het volledige team: dit is de som van alle individuele doelpunten.
# Dus iedere maal een speler een doelpunt maakt wordt het doelpuntsaldo van de ploeg ook
# verhoogd. (private static)
# Vergeet dit ook niet te doen tijdens de __init()__
# • een public static-methode om deze score terug te geven
# 8 7 8
# 6 7 3
# 1 7 3
# 0 0 3
# 7 0 3
# 0 2 2
# Aantal eigen doelpunten speler
# Waarde van de speler (score op 10)
# Ploeg = rode duivels
# Aantal doelpunten ploeg = 17
# Week 08
# Basic Programming (skills) / 6
# Test klasse
# from model.Speler import Speler
# from model.Geboortedatum import Geboortedatum
# # aanspreken van een public static variabele (attribute)
# Speler.naam_ploeg = "Rode duivels"
# sp1 = Speler("Thibault", "Cortois", "keeper", 8, 0)
# sp2 = Speler("Vincent", "Kompany", "aanvaller", 8, 3)
# # par 4 en 5 worden niet opgegeven, zie default par in classe __init__()
# sp3 = Speler("Axel", "Witsel", "aanvaller")
# team = [sp1, sp2, sp3]
# print(team)
# print("\nVincent scoort!")
# sp2.maak_doelpunt()
# print(sp2)
# print("\nAxel scoort!")
# sp3.maak_doelpunt()
# print(sp3)
# print(f"Het doelpunten saldo van { Speler.naam_ploeg } is
# {Speler.get_doelpunten_saldo_ploeg()}")
# Terminal
# [speler: Cortois, Thibault (8/10), speler: Kompany, Vincent (8/10), speler: Witsel,
# Axel (0/10)]
# Vincent scoort!
# speler: Kompany, Vincent (8/10) doelpunten: 4
# Axel scoort!
# speler: Witsel, Axel (0/10) doelpunten: 1
# Het doelpunten saldo van Rode duivels is 5

from modelweek08.Speler import Speler
from modelweek08.Geboortedatum import Geboortedatum

def test_oef1():
    # aanspreken van een public static variabele (attribute)
    Speler.naam_ploeg = "Rode duivels"

    sp1 = Speler("Thibault", "Cortois", "keeper", 8, 0)
    sp2 = Speler("Vincent", "Kompany", "aanvaller", 8, 3)
    sp3 = Speler("Axel", "Witsel", "aanvaller")
    print(sp1)
    team = [sp1, sp2, sp3]
    print(team)

    print(Speler.naam_ploeg)
    print(sp1.naam_ploeg)

    print("\nVincent scoort!")
    sp2.maak_doelpunt()
    print(sp2)

    print("\nAxel scoort!")
    sp3.maak_doelpunt()
    print(sp3)

    print(
        f"Het doelpunten saldo van { Speler.naam_ploeg } is { Speler.get_doelpunten_saldo_ploeg()}")
    pass


test_oef1()


def test_spelers_oef3():
    sp1 = Speler("Thibault", "Cortous", "keeper",
                 8, 0, Geboortedatum(11, 5, 1992))
    sp2 = Speler("Vincent", "Kompany", "aanvaller",
                 8, 3, Geboortedatum(10, 4, 1986))
    sp3 = Speler("Axel", "Witsel", "aanvaller")

    print("\nDe geboortedata van de spelers zijn:")
    for item in [sp1, sp2, sp3]:
        print(f"{item} -> gebootedatum: {item.geboortedatum}")
    pass


test_spelers_oef3()
