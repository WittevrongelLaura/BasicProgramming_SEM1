# Oef 08
# Maak een python applicatie die in staat is om de binnengekomen feedbackscores (van een
# evenement) te verwerken. Hierbij wordt aan een medewerker gevraagd alle feedbackscores
# één voor één in te geven. De medewerker kan afsluiten met een lege score. Op het einde
# worden de scores geteld en afgeprint.
# Geef de verschillende evaluatiecijfers door (sluit af met lege waarde)
# Uitmuntend: A, Zeer goed: B, Goed: C, Voldoende: D, Onvoldoende:
# E, Zwak: F
# Geef de nieuwe feedbackscore op: B
# Geef de nieuwe feedbackscore op: C
# Geef de nieuwe feedbackscore op: A
# Geef de nieuwe feedbackscore op: A
# Geef de nieuwe feedbackscore op: D
# Geef de nieuwe feedbackscore op: A
# Geef de nieuwe feedbackscore op: B
# Geef de nieuwe feedbackscore op: B
# Geef de nieuwe feedbackscore op: C
# Geef de nieuwe feedbackscore op: D
# Geef de nieuwe feedbackscore op: E
# Geef de nieuwe feedbackscore op: D
# Geef de nieuwe feedbackscore op: D
# Geef de nieuwe feedbackscore op: B
# Geef de nieuwe feedbackscore op: B
# Geef de nieuwe feedbackscore op: C
# Geef de nieuwe feedbackscore op: A
# Geef de nieuwe feedbackscore op: A
# Geef de nieuwe feedbackscore op: B
# Geef de nieuwe feedbackscore op: D
# Geef de nieuwe feedbackscore op:
# De gegeven zijn verwerkt. Dit is het resultaat:
# score: A -> aantal: 5
# score: B -> aantal: 6
# score: C -> aantal: 3
# score: D -> aantal: 5
# score: E -> aantal: 1
# score: F -> aantal: 0

dict_evaluaties = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
print("Geef de verschilleden evaluatiecijfers door (sluit af met lege waarde)")
print("Uitmuntend: A, Zeer goed: B, Goed: C, Voldoende: D, Onvoldoende: E, Zwak: F")

feedback_score = input("Geef een score? > ").upper()

while feedback_score != "":
    if feedback_score in dict_evaluaties:
        dict_evaluaties[feedback_score] += 1
    else:
        dict_evaluaties = 1

    feedback_score = input("Geef een score? > ").upper()

print(f"De gegevens zijn verwerkt. Dit is het resultaat:")

for score, aantal in dict_evaluaties.items():
    print(f"score: {score} -> aantal: {aantal}")