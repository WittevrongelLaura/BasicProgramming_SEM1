# Oef 05
# Vraag aan de gebruiker het aantal dagen, uren, minuten en seconden op.
# Bepaal het totale aantal seconden.

dagen = int(input("Geef het aantal dagen op: > "))
uren = int(input("Geef het aantal uren op: > "))
minuten = int(input("Geef het aantal minuten op: > "))
seconden = int(input("Geef het aantal seconden op: > "))

seconden += minuten * 60
seconden += uren * 60 * 60
seconden += dagen * 60 * 60 * 24

print(f"Totaal aantal seconden: {seconden}")