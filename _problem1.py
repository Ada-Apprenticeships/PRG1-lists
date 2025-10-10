playlist = ["Flowers", "Unholy", "As It Was"]
print("Current playlist:", playlist)

playlist.append("Anti-Hero")
playlist.append("Heat Waves")
print("After adding:", playlist)

played = playlist.pop(0)
print(f"Now playing: {played}")
print("Remaining songs:", playlist)

playlist.insert(1, "Blinding Lights")
print("After adding a song:", playlist)

print(f"Next up: {playlist[0]}")
print(f"Total songs: {len(playlist)}")