# Oef 06
# Vraag aan de gebruiker een woord. Overloop deze string. Bewaar alle klinkers samen in één list, de
# medeklinkers in een andere list.
# Print beide lists af. Hoe zorg je ervoor dat zowel hoofdletters als kleine letters in de list terechtkomen?
# Geef een woord op? > Howest
# De gevonden klinkers zijn : ['o', 'e']
# De gevonden medeklinkers zijn: ['h', 'w', 's', 't']

woord = input("Geef een woord op: > ")

klinkers = []
medeklinkers = []

for letter in woord:
    #if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
    if letter in ["a", "e", "i", "o", "u", "y"]:
        klinkers.append(letter)
    else: 
        medeklinkers.append(letter)

print(klinkers)
print(medeklinkers)