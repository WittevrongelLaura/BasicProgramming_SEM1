# Thuis 1
# Vraag aan de gebruiker een woord op. Overloop elk karakter in het woord en tel hierbij het aantal
# klinkers en medeklinkers. Print nadien beide aantallen af.

woord = "woord"
aantal_klinkers = 0
aantal_medeklinkers = 0
for letter in woord:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
        aantal_klinkers += 1
    else:
        aantal_medeklinkers += 1

print(aantal_klinkers)
print(aantal_medeklinkers)