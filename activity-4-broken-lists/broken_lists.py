# Three things below are wrong. Nothing crashes.

FLAGGED = ["Espresso", "Flowers"]


def add_song(playlist, song):
    playlist = playlist.append(song)
    return playlist


def remove_flagged(playlist):
    for song in playlist:
        if song in FLAGGED:
            playlist.remove(song)
    return playlist


def make_backup(playlist):
    backup = playlist
    return backup


queue = ["Levitating", "As It Was"]
print(add_song(queue, "Golden Hour"))

mixed = ["Levitating", "Espresso", "Flowers", "As It Was"]
print(remove_flagged(mixed))

original = ["Levitating", "As It Was"]
saved = make_backup(original)
original.append("Golden Hour")
print(saved)
