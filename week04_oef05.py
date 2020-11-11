# Oef 05
# Maak één list aan met de dagen van de week. Gebruik het printcommando in één codelijn volgende af te
# printen:
# - enkel de werkdagen van de week
# - de weekenddagen van de week
# - de onpare dagen van de week
# - de pare dagen van de week
# Tip: welke techniek zagen we vorige week om een deel uit een string op te halen?
# [‘maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag']
# ['zaterdag', 'zondag']
# ['maandag', 'woensdag', 'vrijdag', 'zondag']
# ['dinsdag', 'donderdag', 'zaterdag']

weekdagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

print(f"De werkdagen: {weekdagen[:5]}")
print(f"De werkdagen: {weekdagen[:-2]}")
print(f"De weekenddagen: {weekdagen[5:]}")
print(f"De weekenddagen: {weekdagen[-2:]}")
print(f"oneven dagen: {weekdagen[::2]}")
print(f"oneven dagen: {weekdagen[0:7:2]}")
print(f"oneven dagen: {weekdagen[1::2]}")
print(f"oneven dagen: {weekdagen[1:7:2]}")