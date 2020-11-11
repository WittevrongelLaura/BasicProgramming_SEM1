# Oef 07
# Vraag aan de gebruiker twee woorden op. Ga na of deze aan elkaar gelijk zijn (zonder rekening te
# houden met kleine letters of hoofdletters)
# Geef een eerst woord: Howest
# Geef een tweede woord: howest
# De woorden Howest en howest zijn gelijk

woord1 = input("Geef een eerste woord in: > ")
woord2 = input("Geef een tweede woord in: > ")

if woord1.lower() == woord2.lower():
    print("Beide woorden zijn gelijk")
else:
    print("Beide woorden zijn verschillend")