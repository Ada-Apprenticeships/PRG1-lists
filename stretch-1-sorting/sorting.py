scores = [72, 38, 55, 91, 40]

print(sorted(scores))
print(sorted(scores, reverse=True))
print(scores)

print("---")

songs = ["as it was", "Blinding Lights", "espresso", "Flowers"]

print(sorted(songs))
print(sorted(songs, key=str.lower))
