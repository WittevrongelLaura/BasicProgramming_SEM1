# Oef 16
# Schrijf een functie ‘geef_even_posities’ die een list als parameter binnenkrijgt. De functie maakt een
# nieuwe list aan, bestaande uit de elementen die op de even posities uit de parameter list staan.
# De elementen uit [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] op de even posities zijn: [0,
# 20, 40, 60, 80]


def geef_even_posities(lijst):
    #resultaat_list = []
    # teller = 0
    # for item in list:
    #     if teller %2 == 0:
    #         resultaat_list.append(item)
    #     teller += 1
    # return resultaat_list

    return lijst[::2]


list1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"De elementen uit {list1} op de even posities zijn: {geef_even_posities(list1)}")
