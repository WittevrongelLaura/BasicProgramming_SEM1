# Maak een functie exclusief_naar_inclusief. Deze ontvangt twee parameters bedrag en btw. Het
# resultaat is het bedrag inclusief btw.
# Je zal de functie als volgt oproepen. Vervolledig de code door zelf de functie exclusief_naar_inclusief te
# schrijven.
# excl_btw = float(input("Hoeveel bedraagt het bedrag exclusief btw? "))
# btw_percentage = float(input("Wat is het btw percentage? "))
# incl_btw = exclusief_naar_inclusief(excl_btw, btw_percentage)
# print(f"Het inclusief bedrag dat je moet betalen is: {incl_btw}")
# Het output zal het volgende zijn.
# Hoeveel bedraagt het bedrag exclusief btw? 200
# Wat is het btw percentage? 1.06
# Het inclusief bedrag dat je moet betalen is: 212

def exclusief_naar_inclusief(bedrag, btw):
    btw_bedrag = (bedrag / 100) * btw
    bedrag_incl_btw = bedrag + btw_bedrag
    return bedrag_incl_btw

excl_btw = float(input("Hoeveel bedraagt het bedrag exclusief btw? > "))
btw_percentage = float(input("Wat is het btw percentage? > "))
incl_btw = exclusief_naar_inclusief(excl_btw, btw_percentage)
print(f"Het inclusief bedrag dat je moet betalen is: {incl_btw}")