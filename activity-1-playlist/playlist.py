playlist = ["Levitating", "As It Was", "Blinding Lights"]

print(f"Starting with {len(playlist)} songs")
print(playlist[0])
print(playlist[-1])

playlist.append("Flowers")
playlist.append("Espresso")
print(f"Now {len(playlist)} songs")

now_playing = playlist.pop(0)
print(f"Now playing: {now_playing}")
print(f"{len(playlist)} left in the queue")

playlist.insert(1, "Golden Hour")
print(f"Next up after this one: {playlist[1]}")

if "Flowers" in playlist:
    playlist.remove("Flowers")
    print("Removed Flowers by request")

print(playlist)
