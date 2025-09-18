# Lists 

You can run the code from the slides if you want.
See `_problem1.py` and `_problem2.py`

## PRIMM Follow-on Tasks

**Remember, this is not a race, you are not expected to complete everything. Take your time.**

### Problem 1

See the code in `problem1_follow_on.py`.

#### Predict
Look at this modified code and predict what will happen:
```python
playlist = ["Song A", "Song B", "Song C"]
playlist.remove("Song B")
playlist = playlist * 2
print(playlist)
```

#### Run
Run the original code and verify your predictions. Note any surprises.

#### Investigate
1. What happens if you try `playlist.pop(10)` when there are only 5 songs?
2. What's the difference between `playlist.remove("Flowers")` and `playlist.pop(0)`?
3. What does `playlist[-1]` give you? What about `playlist[-2]`?

#### Modify
1. Change the code to remove the last song instead of the first
2. Add a check: only add a song if it's not already in the playlist
3. Create a "shuffle" effect by moving the first song to the end

#### Make
Create a new program that:
- Starts with an empty playlist
- Adds 5 songs based on user input
- Removes any duplicate songs
- Prints the playlist in reverse order


### Problem 2

See the code in `problem2_follow_on.py`.

#### Predict
What will this code output?
```python
scores = [80, 90, 85]
scores.sort()
mid = scores[len(scores)//2]
print(f"Median: {mid}")
```

#### Run
Execute the original code and compare with your predictions. Pay attention to how the for loop categorises each score.

#### Investigate
1. What happens if you change `score >= 70` to `70 <= score < 90`?
2. How would `scores.sort()` change the original list? How is this different from `sorted(scores)`?
3. What does the `:.1f` do in the print statement on line 17?

#### Modify
1. Add code to identify "excellent" scores (90 or above)
2. Calculate the median score (middle value when sorted)
3. Find how many scores are above the average
4. Add a letter grade for each score (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: below 60)

#### Make
Create a new program that:
- Takes 6 test scores as input
- Drops the lowest score
- Calculates the average of the remaining 5
- Determines if the student qualifies for honours (average >= 85)
- Displays all information in a formatted report
