# Oef 11
# Gegeven een dictionary waarbij de keys verschillende personen voorstellen en de values de
# bijhorenden landen die bezocht werden. Bijvoorbeeld:
# mijn_team = {
# "Stijn": ["Frankrijk", "Zwitserland", "Oostenrijk", "Nederland"],
# "Christophe": ["USA", "Frankrijk", "Duitsland"],
# "Dieter": ["Nederland", "Duitsland", "Zwitserland", "Oostenrijk"],
# "Gilles": ["UK", "Spanje", "Portugal", "Frankrijk", "Nederland"]
# }
# Schrijf een functie ‘geef_populariteit_landen’ met als parameters bovenstaande dictionary.
# De functie geeft een nieuwe dictionary terug waarbij de landen de keys zijn, en de values
# telkens het aantal bezochte personen. Print nadien alles netjes af.
# Populariteit van de verschillende landen:
# Land: Frankrijk -> aantal: 3
# Land: Zwitserland -> aantal: 2
# Land: Oostenrijk -> aantal: 2
# Land: Nederland -> aantal: 3
# Land: USA -> aantal: 1
# Land: Duitsland -> aantal: 2
# Land: UK -> aantal: 1
# Land: Spanje -> aantal: 1
# Land: Portugal -> aantal: 1

def geef_populaire_bestemmingen(dict):
    dict_aantal_per_land = {}
    for landen in dict.values():
        for land in landen:
            if land in dict_aantal_per_land:
                dict_aantal_per_land[land] += 1
            else:
                dict_aantal_per_land[land] = 1
    return dict_aantal_per_land

mijn_team = {"Stijn": ["Frankrijk", "Zwitserland", "Oostenrijk", "Nederland"],
             "Christophe": ["USA", "Frankrijk", "Duitsland"],
             "Dieter": ["Nederland", "Duitsland", "Zwitserland", "Oostenrijk"],
             "Gilles": ["UK", "Spanje", "Portugal", "Frankrijk", "Nederland"]}

dict_pop = geef_populaire_bestemmingen(mijn_team)
for key, value in dict_pop.items():
    print(f"Land: {key} -> aantal: {value}")