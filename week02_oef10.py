# Oef 10
# Schrijf een functie vergelijking met 4 parameters (a,b,c,d) die getallen voorstellen. De laatste 2
# parameters hebben 0 als default-waarde. De functie geeft het resultaat van volgende berekening terug:
# a – b + c – d.
# - Roep de functie aan door 4 getallen door te geven.
# - Roep de functie aan met dezelfde 4 getallen maar in andere volgorde (gebruik de
# parameternamen)
# - Roep de functie aan met twee getallen.

def vergelijking(a, b, c = 0, d = 0):
    return (a - b) + (c - d)

print(vergelijking(1,2,3,4))
print(vergelijking(c = 2, a = 6, d = 5, b = 2))
print(vergelijking(1,2))