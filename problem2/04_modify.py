# ==============================================================================
# PROBLEM 2 — MODIFY
# ==============================================================================
#
# Each task below asks you to extend the score analyser.
# A working base version is provided each time.
#
# Make one change at a time and run the file to check your result.
#
#   python problem2/04_modify.py
# ==============================================================================

# --- Modify A ---
# Add a third category: "excellent" for scores of 90 or above.
# Scores in `excellent` should NOT also appear in `passed`.
# Think carefully about the order of your if/elif conditions.

print("--- Modify A ---")
scores = [67, 92, 45, 88, 73, 91, 58, 77]
passed = []
failed = []
excellent = []      # ← add logic to populate this

for score in scores:
    if score >= 70:
        passed.append(score)
    else:
        failed.append(score)

print(f"Excellent: {excellent}")
print(f"Passed:    {passed}")
print(f"Failed:    {failed}")


# --- Modify B ---
# Add a letter grade for each score and print them together.
# Grades: A = 90+,  B = 80–89,  C = 70–79,  D = 60–69,  F = below 60

print("\n--- Modify B ---")
scores = [67, 92, 45, 88, 73, 91, 58, 77]

for score in scores:
    # TODO: work out the grade, then print both
    print(f"{score}")       # ← change this to also show the grade


# --- Modify C ---
# Calculate how many scores are above the class average.
# You'll need to calculate the average first, then loop through again.

print("\n--- Modify C ---")
scores = [67, 92, 45, 88, 73, 91, 58, 77]
average = sum(scores) / len(scores)

above_average = 0
# TODO: count how many scores are above the average
print(f"Average: {average:.1f}")
print(f"Above average: {above_average}")
