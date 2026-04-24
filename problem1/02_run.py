# ==============================================================================
# PROBLEM 1 — RUN
# ==============================================================================
#
# Run this file and compare the output to your predictions.
#
#   python problem1/02_run.py
#
# For each line of output, ask yourselves:
#   - Did we get this right?
#   - If not, which part surprised us and why?
#
# Don't move on until you can explain every line of output between you.
# ==============================================================================

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
