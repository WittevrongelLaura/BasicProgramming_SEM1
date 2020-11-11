# Oef 08
# Vraag aan de gebruiker twee int-getallen (gehele getallen) op.
# Bereken nu volgend resultaat: (x + y) * (x + y).
# Print het resultaat af.

x = int(input("Geef een eerste getal op: > "))
y = int(input("Geef een tweede getal op: > "))

resultaat = (x + y) * (x + y)
resultaat2 = (x + y)**2

print(f"({x} + {y}) * ({x} + {y}) = {resultaat}")
print(f"({x} + {y}) ^ 2 = {resultaat2}")
