# Oef 02
# Vraag een niet-decimaal getal aan de gebruiker. Bepaal of het opgegeven getal even of oneven is. Print
# een gepaste boodschap af.

getal = int(input("niet-decimaal getal: > "))

if getal %2 == 0:
    print("even")
else: 
    print("oneven")