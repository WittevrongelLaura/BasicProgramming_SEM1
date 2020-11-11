# Oef 04
# Maak een Python programma dat de leeftijd van een hond vertaalt naar een overeenkomstige leeftijd
# van een mens. Vraag eerst aan de gebruiker de leeftijd van zijn hond. Nadien print je een correcte
# boodschap af waarbij:
# - Indien getal < 0, geef een foutmelding terug.
# - Indien leeftijd = 1 à 14 mensenjaren
# - Indien leeftijd = 2 à 22 mensenjaren
# - Indien meer dan 2: mensenleeftijd = 22 + (jaren – 2) * 5

leeftijd_hond = int(input("Geef de leeftijd van uw hond: > "))

if leeftijd_hond < 0:
    print("Geef een geldige leeftijd in!")
elif leeftijd_hond == 1:
    mensenjaren = 14
elif leeftijd_hond == 2:
    mensenjaren == 22
elif leeftijd_hond > 2:
    mensenjaren = 22 + (leeftijd_hond - 2) * 5
else:
    print("Something went wrong!")

print(f"Deze leeftijd komt overeen met {mensenjaren} mensenjaren")