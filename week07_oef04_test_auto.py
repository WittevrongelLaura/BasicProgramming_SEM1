# Oef 04
# Maak een dataklasse Auto waarbij volgende zaken worden bijgehouden: merk, model,
# kleur, brandstof, km-stand.
# • Maak de gewenste setter en getter properties.
# o Hoe kan je er voor zorgen dat enkel de attributen kmstand en kleur vanuit
# de testklasse gewijzigd kunnen worden?
# • Programmeer de constructor: de methode __init__()
# o De parameters zijn volgende attributen
# § merk, model, kleur, brandstof
# § kleur en brandstof heeft een default waarde van “grijs” en “diesel”.
# § Binnen de constructor geef je de kilometerstand een waarde 0.
# (Deze komt niet binnen via een parameter)
# • Programmeer de methode __str__()
# o De output is “merk (model: model kleur: kleur})”
# • Voeg een extra methode ‘rijden’ met de parameter extra_km toe: hiermee wordt
# de km-stand van de auto verhoogd.
# • Voeg een methode “maak_lawaai” toe die
# • de string bwaahrooah returnt voor een diesel auto
# • de string swooaahsj returnt voor een benzine auto
# • de string sssssssst returnt voor een elektrisch auto
# • de string panne returnt voor alle andere situaties
# Test alles uit: maak een list aan met verschillende voertuigen. Laat vervolgens elk
# voertuig uit de list een random afstand afleggen. Print nadien van elk voertuig de kmstand
# af.
# Je kan hiervoor ook het testbestand op Leho gebruiken.
# import random
# from model.Auto import Auto
# autos = []
# autos.append(Auto("Volkswagen", "passat", "donkergrijs", "diesel"))
# autos.append(Auto("Opel", "astra", "groen", "benzine"))
# autos.append(Auto("Seat", "ibiza", "blauw", "diesel"))
# for auto in autos:
# print(f"Auto {auto} heeft op de kmteller {auto.kmstand}")
# print("\nOp het einde van de dag: ")
# for auto in autos:
# auto.rijden(random.randint(10, 300))
# print(f"\tAuto {auto} heeft op de kmteller {auto.kmstand} en doet
# {auto.maak_lawaai()}")
# Terminal
# Auto Volkswagen (model: passat kleur: donkergrijs) heeft op de kmteller 0
# Auto Opel (model: astra kleur: groen) heeft op de kmteller 0
# Auto Seat (model: ibiza kleur: blauw) heeft op de kmteller 0
# Op het einde van de dag:
# Auto Volkswagen (model: passat kleur: donkergrijs) heeft op de kmteller 118 en doet bwaahrooah
# Auto Opel (model: astra kleur: groen) heeft op de kmteller 257 en doet swooaahsj
# Auto Seat (model: ibiza kleur: blauw) heeft op de kmteller 271 en doet bwaahrooah

import random
from modelweek07.Auto import Auto

# mijn_eerste_auto = Auto("vw", "polo")
# print(f"Dit was een {mijn_eerste_auto.model} {mijn_eerste_auto.merk} {mijn_eerste_auto.kleur}")
# mijn_eerste_auto.kleur = "blauw"
# print(f"nu is hij {mijn_eerste_auto.kleur}")
# #mijn_eerste_auto.merk = "BMW" <--- dit kan niet, geen setter voorzien
# print(f"jammer hij is nooit een {mijn_eerste_auto.merk} geweest")
# print(mijn_eerste_auto)


# print(mijn_eerste_auto.maak_lawaai())

# mijn_eerste_auto.rijden(56)
# print(f"de huidige km stand {mijn_eerste_auto.kmstand}")
# mijn_eerste_auto.rijden(-50)
# print(f"de huidige km stand {mijn_eerste_auto.kmstand}")

autos = []
autos.append(Auto("Volkswagen", "passat", "donkergrijs", "diesel"))
autos.append(Auto("Opel", "astra", "groen", "benzine"))
autos.append(Auto("Seat", "ibiza", "blauw", "diesel"))

for auto in autos:
    print(f"Auto {auto} heeft op de kmteller {auto.kmstand}")
print("\nOp het einde van de dag: ")
for auto in autos:
    auto.rijden(random.randint(10, 300))
    print(
        f"\tAuto {auto} heeft op de kmteller {auto.kmstand} en \
doet {auto.maak_lawaai()}")
