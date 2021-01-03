# Oef 06
# Print alle getallen tussen 200 en 308 (grenzen inclusief) die deelbaar door 7 
# maar geen veelvoud van 5
# zijn.

for getal in range(200, 308):
    if getal %7 == 0 and getal %5 != 0:
        print(getal)