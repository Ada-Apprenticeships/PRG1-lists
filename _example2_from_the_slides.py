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