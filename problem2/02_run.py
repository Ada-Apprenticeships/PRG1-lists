# ==============================================================================
# PROBLEM 2 — RUN
# ==============================================================================
#
# Run this file and compare the output to your predictions.
#
#   python problem2/02_run.py
#
# For each line of output, ask yourselves:
#   - Did we get this right?
#   - If not, which part surprised us and why?
#
# Pay particular attention to:
#   - Whether your pass/fail split was correct
#   - How :.1f formatted the average
#
# Don't move on until you can explain every line of output between you.
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
