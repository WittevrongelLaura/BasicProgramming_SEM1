# Thuis 1
# Schrijf een functie ‘zijn gelijk’ die controleert of 2 lists dezelfde elementen bevatten.

def zijn_gelijk(lijst1, lijst2):
    for element in lijst1:
        if element in lijst2:
            return "minstens 1 gelijk"
    return "Alles verschillend"

list_a = [10, 14, 2, 3, -10]
list_b = [-1, 1, 0, 11, 15]
print(zijn_gelijk(list_a, list_b))