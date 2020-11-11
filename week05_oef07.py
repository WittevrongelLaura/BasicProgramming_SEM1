# Oef 07
# Maak een functie ‘tel_voorkomen_woorden’ met als parameter een string. De functie geeft
# een dictionary terug waarbij de keys de verschillende woorden uit de zin zijn en de bijhorende
# values het aantal keer is dat het woord in de zin voorkomt. Print nadien de dictionary af.
# Onderzochte zin:
# Dit is Howest, is het niet zo? Uiteraard, welkom!
# Dictionary dic_woorden:
# key: dit -> value: 1
# key: is -> value: 2
# key: howest -> value: 1
# key: het -> value: 1
# key: niet -> value: 1
# key: uiteraard -> value: 1
# key: welkom -> value: 1

def tel_voorkomen_woorden(zin):
    dict = {}
    zin = zin.lower()
    zin = zin.replace(",", "").replace("?", "").replace("!", "").replace(".", "")
    list_woorden = zin.split(" ")
    for woord in list_woorden:
        if woord in dict:
            dict[woord] += 1
        else:
            dict[woord] = 1
    return dict

print(tel_voorkomen_woorden("Dit is Howest, is het niet zo? Uiteraard, welkom!"))