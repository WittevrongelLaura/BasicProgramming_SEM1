# Oef 05
# Gegeven het bronbestand scores.txt.
# Dit bronbestand staat in de submap ‘doc’ in. Analyseer het bronbestand: elke lijn bestaat uit de
# gegevens van een student gevolgd door 5 scores.
# Maak nu een applicatie die na het inlezen van het bronbestand op basis van de naam de scores
# van een student(en) kan opzoeken en afprinten, en onmiddellijk ook de gemiddelde score
# afprint.
# Bepaal vooraf welke datastructuur je zal gebruiken om alle data bij te houden.
# Werk vervolgens in deelproblemen:
# • Een functie ‘inlezen_scores_studenten’ staat in voor het inlezen van het bronbestand
# o Welke parameter(s) heeft deze functie nodig?
# o Wat zal deze functie terug geven?
# • Een functie ‘zoek_en_print_student’ zoekt de scores van een student op en print deze
# af.
# o Welke parameter(s) heeft deze functie nodig?
# De scores zijn correct ingelezen.
# Geef de naam van een student op: Blancke
# Resultaat zoekopdracht:
# Gevonden student: Blancke Karen
# Week 06
# Basic Programming (skills) / 4
# De scores van deze student zijn: [16, 15, 17, 15, 18]
# De gemiddelde score is 16.20/20

# ENKEL MCT!
# Gebruik bestand in doc/morsevertaling.txt
# ENKEL MCT!
# Gebruik bestand in doc/spelers.txt

# - Een functie ‘inlezen_scores_studenten’ staat in voor het inlezen van het bronbestand
#  Welke parameter(s) heeft deze functie nodig?
#  Wat zal deze functie terug geven?
# -	Een functie ‘zoek_en_print_student’ zoekt de scores van een student op en print deze af.
#  Welke parameter(s) heeft deze functie nodig?

def inlezen_scores_studenten(bestandsnaam):
    dict_studenten = {}
    fo = open(bestandsnaam)
    lijn = fo.readline().rstrip("\n")
    while lijn != "":
        # verwerken van 1 lijn
        delen_lijn_list = lijn.split(":")
        dict_studenten[delen_lijn_list[0]] = [int(delen_lijn_list[1]), int(delen_lijn_list[2]), int(
            delen_lijn_list[2]), int(delen_lijn_list[3]), int(delen_lijn_list[4]), int(delen_lijn_list[5])]
        lijn = fo.readline().rstrip("\n")
    fo.close()

    return dict_studenten


def zoek_en_print_student(dict_studenten, deel_naam):
    for naam, punten in dict_studenten.items():
        if deel_naam in naam:
            print(f"gevonden: {naam}")
            print(f"met volgende punten: {punten}")
            print(f"het gem is: {sum(punten) / len(punten)}")


dict_howest = inlezen_scores_studenten('docweek06/scores.txt')
print(f"{dict_howest}")
zoekopdracht = input("Welke studenten wil je vinden? > ")
zoek_en_print_student(dict_howest, zoekopdracht)
