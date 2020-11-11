# Thuis 1
# Om de prijs van een woning te bepalen, telt men de prijs van de bouwgrond en de eigenlijke bouw op.
# Het btw-tarief op dit totaal is 21 %.
# Je vraagt aan de gebruiker de prijs van de bouwgrond en de prijs van het gebouw.
# Je toont het totaal te betalen bedrag.

prijs_bouwgrond = float(input("Prijs van de bouwgrond? > "))
prijs_gebouw = float(input("Prijs van het gebouw? > "))

prijs_woning_excl_btw = prijs_bouwgrond + prijs_gebouw
btw = prijs_woning_excl_btw / 100 * 21
prijs_woning_incl_btw = prijs_woning_excl_btw + btw

print(f"De totale kostprijs van het project is: {prijs_woning_incl_btw:.2f}")
