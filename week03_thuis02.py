# Thuis 2
# Vraag aan de gebruiker een woord op. Overloop elk karakter in het woord en schrap alle klinkers.


woord = "woord"
nieuw_woord = ""
for letter in woord:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
        letter = "*"
        nieuw_woord += letter
    else: 
        nieuw_woord += letter  

print(nieuw_woord)