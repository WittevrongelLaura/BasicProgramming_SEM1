# Oef 10
# Maak een applicatie dat aan de gebruiker een aantal in te voeren producten vraagt. Vervolgens loop je
# dat aantal af en vraag je telkens bij elk product op:
# - De categorie op: de gebruiker kiest tussen “Groente”, “Fruit”, “Drank”.
# - De kostprijs van het product
# Print op het einde per categorie de totale kost op, alsook de gemiddelde prijs per categorie af.
# Voorbeeld:
# Geef het aantal producten op dat u wenst in te voeren:> 5
# Wat is de categorie? [G: Groente, F: Fruit, D: Drank]> D
# Wat is de kostprijs van het product?> 10
# Wat is de categorie? [G: Groente, F: Fruit, D: Drank]> D
# Wat is de kostprijs van het product?> 20
# Wat is de categorie? [G: Groente, F: Fruit, D: Drank]> G
# Wat is de kostprijs van het product?> 12.6
# Wat is de categorie? [G: Groente, F: Fruit, D: Drank]> F
# Wat is de kostprijs van het product?> 4
# Wat is de categorie? [G: Groente, F: Fruit, D: Drank]> G
# Wat is de kostprijs van het product?> 8.7
# 2 producten zitten in de categorie Groenten
# Totale kostprijs: 21.3
# Gemiddelde prijs per product: 10.65
# 1 producten zitten in de categorie Fruit
# Totale kostprijs: 4.0
# Gemiddelde prijs per product: 4.00
# 2 producten zitten in de categorie Drank
# Totale kostprijs: 30.0
# Gemiddelde prijs per product: 15.00

aantal_prod = int(input("Wat is het aantal producten dat u wenst in te voeren? > "))
aantal_groenten = 0
aantal_fruit = 0
aantal_drank = 0
tot_prijs_g = 0
tot_prijs_f = 0
tot_prijs_d = 0

for product in range(0, aantal_prod):
    categorie = input("Wat is de categorie? [G: groente, F: fruit, D: drank] > ")
    prijs = float(input("Wat is de kostprijs van het product? > "))

    if categorie.lower() == "g":
        aantal_groenten += 1
        tot_prijs_g += prijs
    elif categorie.lower() == "f":
        aantal_fruit += 1
        tot_prijs_f += prijs
    elif categorie.lower() == "d":
        aantal_drank += 1
        tot_prijs_d += prijs
    else:
        print("Hello??")

print(f"{aantal_groenten} product(en) zitten in de categorie groenten\nTotale kostprijs: {tot_prijs_g:.2f}\nGemiddelde prijs per product: {tot_prijs_g/aantal_groenten:.2f}")

print(f"{aantal_fruit} product(en) zitten in de categorie groenten\nTotale kostprijs: {tot_prijs_f:.2f}\nGemiddelde prijs per product: {tot_prijs_f/aantal_fruit:.2f}")

print(f"{aantal_drank} product(en) zitten in de categorie groenten\nTotale kostprijs: {tot_prijs_d:.2f}\nGemiddelde prijs per product: {tot_prijs_d/aantal_drank:.2f}")
