# ==============================================================================
# PROBLEM 2 — PREDICT
# ==============================================================================
#
# Read the code below carefully. DO NOT run it yet.
#
# In your pairs, write down your answers to these questions:
#
#   1. How many scores end up in `passed`? How many in `failed`?
#      (Go through the list one by one: 67, 92, 45, 88, 73, 91, 58, 77)
#
#   2. What will max(scores) and min(scores) return?
#
#   3. The average is calculated as sum(scores) / len(scores).
#      Roughly what do you expect the average to be? (You don't need to
#      calculate it exactly — a ballpark is fine.)
#
#   4. What does :.1f do in the f-string on the average line?
#      Will the average be rounded, truncated, or something else?
#
#   5. What will the pass rate line print?
#
# Write your predictions down before moving to 02_run.py
# ==============================================================================

scores = [67, 92, 45, 88, 73, 91, 58, 77]
print(f"All scores: {scores}")

passed = []
failed = []

for score in scores:
    if score >= 70:
        passed.append(score)
    else:
        failed.append(score)

print(f"Passing scores: {passed}")
print(f"Failing scores: {failed}")

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

print(f"Highest: {highest}, Lowest: {lowest}")
print(f"Class average: {average:.1f}")
print(f"Pass rate: {len(passed)}/{len(scores)}")
