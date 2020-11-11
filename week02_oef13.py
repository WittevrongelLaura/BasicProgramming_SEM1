# Oef 12
# Schrijf een functie vertaal_maandnummer_naar_str die een maandnummer binnenkrijgt als parameter.
# Controleer in de functie of het getal tussen 1 en 12 ligt. Geef nadien de corresponderende maand terug.
# Indien buiten het interval, geef je een foutboodschap terug. Test de functie met meerdere
# maandnummers.
# Nadien test je je functie door volgende input aan de gebruiker te vragen.
# Geef een maandnummer: 9
# De overeenkomstige maand is -> september
# Geef een maandnummer: 13
# De overeenkomstige maand is -> onbekende maand

def geef_celsius(temp_fah):
    celsius = (temp_fah - 32) * (5/9)
    return celsius

def geef_fahrenheit(temp_cel):
    fahrenheit = (temp_cel * 9 / 5) + 32
    return fahrenheit

eenheid = input("Welke eenheid gebruikt u? [C: Celsius, F: Fahrenheit] > ")
if eenheid.lower() == "c":
    temp_celsius = float(input("Geef een temperatuur in Celsius op: > "))
    print(f"De overeenkomstige temperatuur in Fahrenheit is: {geef_fahrenheit(temp_celsius):.2f}")
else:
    temp_fahrenheit = float(input("Geef een temperatuur in Fahrenheit op: > "))
    print(f"De overeenkomstige temperatuur in Celsius is: {geef_celsius(temp_fahrenheit):.2f}")