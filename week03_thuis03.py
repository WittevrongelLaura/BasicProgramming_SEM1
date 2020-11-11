# Thuis 3
# Vraag aan de gebruiker twee jaartallen op. Print de schrikkeljaren tussen deze twee jaartallen af.
# Hergebruik hiervoor defunctie ‘is_schrikkeljaar’ waarbij getest wordt of een jaartal al dan niet een
# schrikkeljaar is.


def is_schrikkeljaar(jaartal):
    if jaartal %4 == 0 and jaartal %100 != 0:
        return True
    elif jaartal %100 == 0 and jaartal %400 == 0:
        return True
    else:
        return False

jaartal1 = 1993
jaartal2 = 2005

for jaartal in range(jaartal1, jaartal2):
    if is_schrikkeljaar(jaartal):
        print(jaartal)