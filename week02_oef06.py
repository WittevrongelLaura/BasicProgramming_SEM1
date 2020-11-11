# Oef 06
# Controleer of Python bij het vergelijken van 2 strings al dan niet hoofdlettergevoelig is.
# Geef een eerst woord: Howest
# Geef een tweede woord: howest
# De woorden Howest en howest zijn niet gelijk

woord1 = input("Geef een eerste woord in: > ")
woord2 = input("Geef een tweede woord in: > ")

if woord1 == woord2:
    print("Beide woorden zijn gelijk")
else:
    print("Beide woorden zijn verschillend")