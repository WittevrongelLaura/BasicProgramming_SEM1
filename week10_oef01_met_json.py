# Deel 2: inlezen van een json-file
# 1: Plaast het bestand ‘personen.json’ in de submap ‘doc’.
# Bestudeer aandachtig het json-bestand, controleer waar er [] en {} staat . Welke data
# vind je precies terug?
# 2: In de submap ‘model’ voeg je een extra klasse PersoonRepository toe om de json in
# te lezen en te filteren.
# 3: PersoonRepository:
# • Voeg een public static methode ‘inlezen_ouders_met_studenten’ toe die in
# staat is om het bronbestand in te lezen en een list van ouders met hun
# studenten terug te geven.
# Opgelet: tijdens het verwerken van de data van een ouder lees je ook de
# studenten mee in. Maak dus eerst een object van de klasse Ouder aan, waarna
# Persoon
# Student Docent Ouder
# Auto
# Week 10
# Basic Programming (skills) / 5
# er 0 of meerdere objecten van de klasse Student via de methode
# voeg_student_toe toegevoegd worden.
# • Opgelet: je zal zien dat er geen studentnummer in de json file terug te vinden
# is.
# Geef een student dus een random studentennummer tussen 1 en 10000, als je
# een student aanmaakt.
# Test de methode uit. Nadien print je van alle ingelezen ouders de verschillende
# opleidingen (geen dubbels) van hun kinderen af. Gebruik hiervoor de juiste methode
# uit de klasse Ouder.

# 3: Zoekopdracht
# Voeg de static methode ‘filter_ouders_met_studenten_uit_opleiding’ toe aan de
# klasse PersoonRepository. Deze methode heeft als parameters de ingelezen list met
# ouders én een een opleidingsnaam. De ouders worden in de methode overlopen:
# enkel deze ouders waarvan één of meerdere studenten de doorgegeven opleiding
# volgen, worden in een list op het einde terug gegeven.

from modelweek10_1.PersoonRepository import PersoonRepository


def test_json_deel1():
    list_ouders = PersoonRepository.inlezen_ouders_met_studenten()
    print(list_ouders)
    for ouder in list_ouders:
        print(ouder.geef_info_studenten())

    print("Lijst van ouders met de opleidingen die hun kinderen volgen:")
    for ouder in list_ouders:
        print(
            f"De kinderen van {ouder} volgen deze opleidingen: {ouder.geef_opleidingen_studenten()}")


def test_json_deel2():
    list_ouders = PersoonRepository.inlezen_ouders_met_studenten()
    naam_opleiding = input("\nGeef een opleiding op:> ")
    list_resultaat = PersoonRepository.filter_ouders_met_studenten_uit_opleiding(
        list_ouders, naam_opleiding)
    print("Resultaat zoekopdracht: ")
    for ouder in list_resultaat:
        print(f"{ouder} heeft student(en) die de opleiding {naam_opleiding} volgen.")


test_json_deel1()
test_json_deel2()
