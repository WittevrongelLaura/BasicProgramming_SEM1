# Afwerking labo week 7:
# Werk de opgaven van laboweek 7 af. In de startbestanden vind je de laatste versie van de klasse
# Winkelkar terug.
# • Zorg er voor dat de +-operator toegepast kan worden:
# o zodat twee winkelkarretjes bij elkaar kunnen opgeteld worden en een nieuw
# winkelkarretje opleveren (welke methode moet hiervoor toegevoegd worden?)
# o zodat het bestaande winkelkarretje uitgebreid wordt met de producten uit een andere
# winkelkarretje (welke methode moet hiervoor toegevoegd worden?)
# • Tel beide winkelkarretjes op via de plus-operator. Print resultaat af.
# from model.Winkelkar import Winkelkar
# action_kar = Winkelkar()
# action_kar.voeg_product_toe("cd1")
# action_kar.voeg_product_toe("cd2")
# action_kar.voeg_product_toe("cd3")
# action_kar.voeg_product_toe("cd4")
# action_kar.verwijder_product("cd3")
# ikea_kar = Winkelkar()
# ikea_kar.voeg_product_toe("Billy")
# ikea_kar.voeg_product_toe("Factum")
# print(f"Winkelkar 1: {action_kar}")
# print(f"Winkelkar 2: {ikea_kar}")
# print("***** Winkelkar 3 = Winkelkar 1 + Winkelkar 2 *****")
# kerst_kar = action_kar + ikea_kar
# print(f"Winkelkar 3: {kerst_kar}")
# print("***** Winkelkar 1 +=Winkelkar 2 *****")
# action_kar += ikea_kar
# print(f"Winkelkar 1: {action_kar}")
# Terminal
# Winkelkar 1: De winkelkar bestaat uit 3: ['cd1', 'cd2', 'cd4']
# Winkelkar 2: De winkelkar bestaat uit 2: ['Billy', 'Factum']
# ***** Winkelkar 3 = Winkelkar 1 + Winkelkar 2 *****
# Winkelkar 3: De winkelkar bestaat uit 5: ['cd1', 'cd2', 'cd4', 'Billy',
# 'Factum']
# ***** Winkelkar 1 +=Winkelkar 2 *****
# Winkelkar 1: De winkelkar bestaat uit 5: ['cd1', 'cd2', 'cd4', 'Billy',
# 'Factum']

from modelweek08.Winkelkar import Winkelkar

action_kar = Winkelkar()
action_kar.voeg_product_toe("cd1")
action_kar.voeg_product_toe("cd2")
action_kar.voeg_product_toe("cd3")
action_kar.voeg_product_toe("cd4")
action_kar.verwijder_product("cd3")

ikea_kar = Winkelkar()
ikea_kar.voeg_product_toe("Billy")
ikea_kar.voeg_product_toe("Factum")

print(f"Winkelkar 1: {action_kar}")
print(f"Winkelkar 2: {ikea_kar}")


# NIEUW WEEK 08
print("***** Winkelkar 3 = Winkelkar 1 + Winkelkar 2 *****")
kerst_kar = action_kar + ikea_kar
print(f"Winkelkar 3: {kerst_kar}")
print("***** Winkelkar 1 += Winkelkar 2 *****")
action_kar += ikea_kar
print(f"Winkelkar 1: {action_kar}")
