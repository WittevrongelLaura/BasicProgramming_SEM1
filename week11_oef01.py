# Oef 01
# Gegeven onderstaande methode (zie bronmateriaal).
# Vervang alle print-opdrachten door log-opdrachten.
# Test even uit wat de verschillende log-levels precies inhouden.
# Hoe kan men het formaat van een log-bericht beïnvloeden?
# Hoe kan men naast het scherm ook naar een bestand loggen?
# Meer info vind je alvast hier:
# https://docs.python.org/3.9/howto/logging.html#logging-basic-tutorial

import random
import logging

# oef 1


def genereer_even_getallen(aantal):
    logging.basicConfig(filename="log_evengetallen.log", level=logging.INFO, format="%(asctime)s - %(message)s")
    even_getallen = []

    while len(even_getallen) != aantal:
        getal = random.randint(0, 1000)
        logging.debug(f"Gekozen getal: {getal}")
        if getal % 2 == 0 and getal not in even_getallen:
            even_getallen.append(getal)
    logging.info(f"De lijst met even getallen: {even_getallen}")
    return even_getallen


aantal = int(input("Geef een aantal getallen op:> "))
resultaat = genereer_even_getallen(aantal)
print(f"De gekozen even getallen zijn: {resultaat} ")