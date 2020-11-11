# Oef 12
# Vraag aan de gebruiker een woord, print vervolgens elk karakter onder elkaar af.

woord = input("Geef een woord op > ")

for letter in woord:
    print(letter)
#of
for letter in range(0, len(woord)):
    print(woord[letter])