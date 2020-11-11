# Oef 13
# Schrijf een functie ‘swap’ die twee strings binnenkrijgt. De functie stelt één nieuwe string op waarbij de
# twee letters van elk woord worden omgewisseld en beide nieuwe woorden door een spatie gescheiden
# worden.
# Het resultaat van de functie is de nieuwe string.
# Voorbeeld: “abc” en “xyz” à “xyc abz”

def swap(woord1, woord2):
    nieuw_woord1 = woord1[:2] + woord2[2:]
    nieuw_woord2 = woord2[:2] + woord1[2:]
    return f"{nieuw_woord1} {nieuw_woord2}"

print(swap("laura", "tibau"))