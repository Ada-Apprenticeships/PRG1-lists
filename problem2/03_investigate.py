# ==============================================================================
# PROBLEM 2 — INVESTIGATE
# ==============================================================================
#
# Each block below is a small experiment. For each one:
#   - Read the question in the comment
#   - Predict what will happen
#   - Uncomment the code and run JUST that block to check
#   - Talk through what you found
#
# Run this file each time:   python problem2/03_investigate.py
# ==============================================================================

# --- Investigation A ---
# The pass boundary is currently score >= 70.
# What happens to the split if you change it to 70 <= score < 90?
# Which scores would be "passed"? Which would fall through?

scores = [67, 92, 45, 88, 73, 91, 58, 77]
passed = []
failed = []
# for score in scores:
#     if 70 <= score < 90:      # ← changed condition
#         passed.append(score)
#     else:
#         failed.append(score)
# print("Passed:", passed)
# print("Failed:", failed)


# --- Investigation B ---
# .sort() changes the list in place. sorted() returns a NEW list and
# leaves the original unchanged.
# Predict: what does each print statement show?

scores = [67, 92, 45, 88, 73, 91, 58, 77]
# sorted_scores = sorted(scores)
# print("original after sorted():", scores)
# print("new list from sorted():  ", sorted_scores)

# scores.sort()
# print("original after .sort():  ", scores)


# --- Investigation C ---
# :.1f controls how a float is displayed — it means "1 decimal place".
# What do :.2f and :.0f produce?

average = 73.875
# print(f":.1f  →  {average:.1f}")
# print(f":.2f  →  {average:.2f}")
# print(f":.0f  →  {average:.0f}")


# --- Investigation D ---
# How would you find the median (middle value) of a sorted list?
# This uses integer division //  to find the middle index.
# Predict: what is mid for this 3-item list?

scores = [80, 85, 90]
scores.sort()
# mid = scores[len(scores) // 2]
# print("Median:", mid)
