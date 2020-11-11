# Oef 13
# Schrijf een functie ‘tel_elementen_binnen_interval’ met drie parameters: een list, een minimum en een
# maximum. De functie telt hoeveel elementen uit de list binnen het interval [min, max] vallen en geeft dat
# aantal terug.
# List1: [10, 20, 30, 40, 40, 40, 70, 80, 99]
# Het aantal elementen tussen 40 en 100 bedraagt: 6
# List2: ['a', 'b', 'c', 'd', 'e', 'f']
# Het aantal elementen tussen a en e bedraagt: 5

def tel_elementen_binnen_interval(lijst, min, max):
    aantal = 0
    for element in lijst:
        if element <= max and element >= min:
            aantal += 1
    return f"Het aantal elementen tussen {min} en {max} zijn: {aantal}"

list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']


print(tel_elementen_binnen_interval(list1, 40, 100))
print(tel_elementen_binnen_interval(list2, "a", "e"))