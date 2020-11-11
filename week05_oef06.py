# Oef 06
# Maak een methode ‘voeg_niew_element_toe’ aan die een nieuw element aan een dictionary
# toevoegt nadat er eerst gecontroleerd wordt of de key nog niet in gebruik is. Indien de key wel
# reeds in gebruik is, wordt er een foutboodschap afgeprint.
# De methode heeft als parameters de key, de value en de dictionary zelf.
# Test dit uit door aan dictionary Howest achtereenvolgens toe te voegen
# - Element met key ‘1IPO’ met waarde ‘51’
# - Element met key ‘1IPO’ met waarde ‘10’
# Print nadien de dictionary Howest af (via methode uit eerdere oefening).
# Toevoeging nieuw element geslaagd.
# Toevoegen mislukt. Key 1IPO reeds aanwezig!
# Dictionary Howest:
# key: 1MCT -> value: 101
# key: 2MCT -> value: 88
# key: 3MCT -> value: 77
# key: 1MIT -> value: 58
# key: 2MIT -> value: 36
# key: 1Devine -> value: 123
# key: 2Devine -> value: 98
# key: 3Devine -> value: 55
# key: 1IPO -> value: 51

def voeg_nieuw_element_toe(key, value, dict):
    if key in dict:
        print("De key bestaat al")
    else: 
        dict[key] = value
    return dict

def print_dictionary(dict):
    for key, value in dict.items():
        print(f"key: {key} -> value: {value}")

MCT = {"1MCT": 131, "2MCT": 88, "3MCT": 77}
MIT = {"1MIT": 58, "2MIT": 36}
Devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

print_dictionary(voeg_nieuw_element_toe("4MCT", 1000, MCT))