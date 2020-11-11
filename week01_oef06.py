# Oef 06
# Vraag aan de gebruiker een aantal seconden op.
# Zet dit aantal om in dagen, uren, minuten en seconden.
seconden = int(input("Geef het aantal seconden op: > "))

dagen = seconden // (60 * 60 * 24)
restsec = seconden % (60 * 60 * 24)

uren = restsec // (60 * 60)
restsec = restsec % (60 * 60)

minuten = restsec // 60
restsec = restsec % 60

print(f"d:h:m:s -> {dagen}:{uren}:{minuten}:{restsec}")