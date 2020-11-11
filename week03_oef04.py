# Oef 04
# Print alle oneven getallen tussen 10 en 129 naast elkaar af. Gebruik een for-lus.
reeks =""
for getal in range(10, 129 + 1):
    if getal %2 != 0:
        reeks += f"{getal} - "

if reeks.endswith("- "):
    reeks = reeks[:-2]

print(reeks)