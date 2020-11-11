# Oef 03
# Maak volgende 3 dictionaries aan. Ze stellen beide de verschillende studentenaantallen per
# opleidingsjaar voor.
# - ‘MCT’ met de elementen {"1MCT": 131, "2MCT": 88, "3MCT": 77}
# - ‘MIT’ met de elementen {“1MIT”: 58, “2MIT”: 36}
# - ‘devine’ met de {"1Devine": 123, "2Devine": 98, "3Devine": 55}
# Geef een antwoord op onderstaande vragen d.m.v. een kort codevoorbeeld op bovenstaande
# dictionaries:
# - Wat is het effect van het print-commando op een dictionary?
# - Hoe kan je een element uit de dictionary opvragen?
# - Hoe voeg je een nieuw element aan een dictionary toe?
# - Wat gebeurt er als een nieuw element met dezelfde key aan een dictionary
# toegevoegd wordt?
# - Hoe controleer je of een key in een dictionary reeds in gebruik is?
# - Hoe kan je een key (met value) uit een dictionary verwijderen? Wat als key niet
# aanwezig is?

MCT = {"1MCT": 131, "2MCT": 88, "3MCT": 77}
MIT = {"1MIT": 58, "2MIT": 36}
Devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

#effect print commando
print(MCT)

#element opvragen
print(MCT["1MCT"])

#nieuw element toevoegen
MCT["4MCT"] = 11
print(MCT)

#nieuw element met dezelfde key toevoegen
MCT["4MCT"] = 111
print(MCT)

#controleren of een key reeds in gebruik is
if "1MCT" in MCT:
    print("bestaat")
else: 
    print("bestaat niet")

#controleren of value in een dict staat
if 111 in MCT.values():
    print("value bestaat")
else:
    print("value bestaat niet")

#key met value verwijderen
del MCT["4MCT"]
print(MCT)