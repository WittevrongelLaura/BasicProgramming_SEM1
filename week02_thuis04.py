# Thuis 5
# Schrijf een functie stopafstand die de remafstand van een voertuig berekent. De formule hiervoor vind
# je hieronder. (Bepaal hieruit zelf welke parameters deze functie moet hebben).
# Test voldoende uit.
# stopafstand = reactieweg + remweg
# = snelheid * reactietijd + (snelheid)² / (2 * remvertraging)
# Hou rekening met:
# - De snelheid dient omgezet te worden in m/s.
# De omzetting van km/u naar m/s gebeurt door een deling van 3,6
# • Bv: 50 km/u à 50/3,6 à13,89 m/s
# - De reactieweg is de afstand afgelegd tussen het moment van waarneming en het moment
# van de reactie (het remmen).
# - De remweg is de afstand om bij een bepaalde snelheid volledig tot stilstand te komen.
# De snelheid van het voertuig die tijdens het remmen per seconde afneemt, noemt men de
# remvertraging. Dit wordt aangeduid met m/sec². Voor een personenauto bedraagt dit bij een droog
# wegdek 8 m/sec², bij een natwegdek 5 m/sec².


def stopafstand_1(reactie, rem, snel):
    return reactie + rem

def stopafstand_2(snel):
    snel_in_ms = snel /3.6
    reactie = 1 ##1 sec voor een alerte chauffeur
    remvertraging = 8 #8m/sec^2 op droog wegdek

    return snel_in_ms * reactie + (snel_in_ms)**2 / (2*remvertraging)

snelheid = int(input("wat is de snelheid? "))
reactieweg = int(input("Wat is de reactieweg? "))
remweg = int(input("Wat is de remweg? "))

print(f"De stopafstand is {stopafstand_1(reactieweg, remweg, snelheid)}")
print(f"De stopafstand2 is {stopafstand_2(snelheid)}")