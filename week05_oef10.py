# Oef 10
# Gegeven een dictionary waarbij de keys verschillende personen voorstellen en de values de
# bijhorenden landen die bezocht werden. Bijvoorbeeld:
# mijn_team = {
# "Stijn": ["Frankrijk", "Zwitserland", "Oostenrijk", "Nederland"],
# "Christophe": ["USA", "Frankrijk", "Duitsland"],
# "Dieter": ["Nederland", "Duitsland", "Zwitserland", "Oostenrijk"],
# "Gilles": ["UK", "Spanje", "Portugal", "Frankrijk", "Nederland"]
# }
# Schrijf een functie ‘filter_op_land’ met als parameters bovenstaande dictionary en een
# gezocht land. De functie geeft in een list alle personen terug die dit land bezocht hebben.
# Geef een land op:> Nederland
# Deze personen hebben reeds dit land bezocht: ['Stijn', 'Dieter',
# 'Gilles']

def filter_op_land(dict, gezocht_land):
    list_land_bezocht = []
    for persoon, list_landen in dict.items():
        if gezocht_land in list_landen:
            list_land_bezocht.append(persoon)
    return list_land_bezocht

mijn_team = {"Stijn": ["Frankrijk", "Zwitserland", "Oostenrijk", "Nederland"],
             "Christophe": ["USA", "Frankrijk", "Duitsland"],
             "Dieter": ["Nederland", "Duitsland", "Zwitserland", "Oostenrijk"],
             "Gilles": ["UK", "Spanje", "Portugal", "Frankrijk", "Nederland"]}

#gezocht_land = input("Geef een land op:> ").capitalize()
gezocht_land = "Frankrijk"
print(f"Deze personen hebben reeds dit land bezocht: {filter_op_land(mijn_team, gezocht_land)}")
