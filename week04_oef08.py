# Oef 08
# Maak een functie ‘kies_element’ aan met als parameter een list. De functie kiest een willekeurig element
# uit de doorgegeven list en geeft deze terug. Test deze functie met
# - een list met strings, nl. de verschillende maanden
# - een list met getallen
# Tip: Gebruik de documentatie van de module Random en zoek hoe je een willekeurige waarde uit een list
# kan opvragen. (Onder welke “groep” binnen de Data Types valt een list volgens de theorie les (zie
# schema))
# Print telkens het gekozen element af.
import random

def kies_element(lijst):
    return random.choice(lijst)

maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober","november", "decemeber"]
getallen = [100, 200, 300, 400]

print(f"een willekeurig element uit {maanden} is {kies_element(maanden)}")
print(f"een willekeurig element uit {getallen} is {kies_element(getallen)}")