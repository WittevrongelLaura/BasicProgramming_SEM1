# Oef 04a
# Voor deze opgave staat de klasse Hotelgast uit het labo van week 7 reeds gekopieerd in het
# startbestand.
# Maak nu een nieuwe klasse Hotel die naast de naam van het hotel ook de gastenlijst bijhoudt.
# Voorzie de klasse Hotel nu van
# • De klassieke methodes __init__() en __str__()
# o Je kan de parameters van de constructor afleiden uit de test klasse.
# • Property om de naam van het Hotel op te vragen en te wijzigen
# (controleer of de naam geen lege string is)
# • Voor de gasten maak je een lege list aan in de init-methode. Daarna voorzie je hiervoor
# enkel een get-property.
# o Als je straks een list van gasten wilt printen, voldoet de __str__() methode in de
# class Hotelgast?
# • Programmeer de methode __str__(): De output is “Hotel: naam”
# Voeg aan de klasse Hotel de methode check_in(naam, voornaam) toe:
# • Deze methode heeft als parameters de naam en voornaam van de nieuwe gast.
# • Maak in deze methode een object van de klasse Hotelgast.
# o Waarop moet je letten bij het importeren van de klasse Hotelgast????
# • Controleer vooraf of deze nieuwe hotelgast reeds niet in de list aanwezig is.
# o Voordat je dit kan doen, moet je (of Python) natuurlijk kunnen controleren
# wanneer 2 hotelgasten aan elkaar gelijk zijn. Pas de klasse Hotelgast aan.
# • Indien nog niet in het Hotel aanwezig:
# o Wijzig de property ‘is_ingecheckt’ van de nieuwe hotelgast naar True.
# o Voeg de nieuwe hotelgast toe aan de list gasten.
# o Print in de methode de boodschap: Correct ingecheckt: \n hotelgast
# • Indien de hootelgast wel al aanwezig was, dan print je een foutboodschap af.
# Voeg aan de klasse Hotel de print_info_gasten() toe:
# • De output van deze functie kan je afleiden uit de test klasse.
# Test de dataklasse al eens uit!

# Oef 04b
# Voeg aan de klasse Hotel de private methode __zoek_hotelgast(naam,voornaam) toe.
# • Deze methode heeft als parameters de naam en voornaam
# • Maak in deze methode een (tijdelijk) object hotelgast aan
# • Overloop de list met gasten en ga op zoek naar het (tijdelijk) object hotelgast dat hiermee
# overeenstemt:
# o Indien teruggevonden: geef het gevonden object terug
# o Indien niet teruggevonden: geef None terug
# Voeg aan de klasse Hotel de methode check_out(naam, voornaam) toe:
# • Deze methode heeft als parameters de naam en voornaam van de gast.
# • Gebruik de private methode __zoek_hotelgast() om de bijhorende gast terug te vinden:
# o Hotelgast is teruggevonden. Controleer eerst of zijn saldo nul is. Pas dan mag de
# hotelgast uit de list verwijderd worden. Is het saldo nog niet nul: geef een gepaste
# foutmelding.
# o Indien de hotelgast niet teruggevonden wordt, print je een gepaste foutmelding
# af.

# Oef 04c
# Voeg aan de klasse de methode bestel_drank(naam,voornaam,kostprijs) toe:
# • Deze methode heeft als parameters de naam en voornaam van de gast, en de kostprijs van
# de bestelde drank.
# • Gebruik de private methode __zoek_hotelgast() om de bijhorende gast terug te vinden:
# o Hotelgast is teruggevonden. Verhoog zijn saldo met de doorgegeven kostprijs.
# o Indien de hotelgast niet teruggevonden wordt, print je een gepaste foutmelding
# af.
# Voeg aan de klasse de methode vereffen_saldo_gast(naam,voornaam) toe:
# • Deze methode heeft als parameters de naam en voornaam van de gast.
# • Gebruik de private methode __zoek_hotelgast() om de bijhorende gast terug te vinden:
# o Hotelgast is teruggevonden. Zet het saldo op nul.
# o Indien de hotelgast niet teruggevonden wordt, print je een gepaste foutmelding
# af.


from modelweek08.Hotel import Hotel
# from model.Hotelgast import Hotelgast

hotel_howest = Hotel("Howest")
print(hotel_howest)

hotel_howest.check_in("Walcarius", "Stijn")
hotel_howest.check_in("Laprudence", "Christophe")
hotel_howest.check_in("Walcarius", "Stijn")

hotel_howest.bestel_drank("Walcarius", "Stijn", 100)

print("\n")
hotel_howest.print_info_gasten()
print("Stijn betaalt zijn schuld")
hotel_howest.vereffen_saldo_gast("Walcarius", "Stijn")
print("******************")
hotel_howest.check_out("Walcarius", "Stijn")
print("******************")
print("\n")
hotel_howest.print_info_gasten()
