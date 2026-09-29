# Activity 2: Analysing scores

File: `score_analysis.py`

Ten exam results in, a report out: how many passed, the spread, and who needs
help.

## Predict

- How many pass and how many fail?
- What is the pass rate?
- What does the final line print, and in what order?

## Run

Execute and compare.

## Investigate

- Two empty lists are created before the loop and filled during it. Why do they
  have to exist before the loop starts?
- A score of exactly 40 appears in the data. Which list does it end up in, and
  which character in the code decides that? You have met this question twice
  already this week.
- `sum`, `max`, `min` and `len` all take the whole list at once. How is that
  different from the accumulator loops you wrote on Day 3, and when would you
  still need a loop?
- The final line sorts `failed` but the list itself is unchanged afterwards.
  Hold that thought until activity 3.

## Modify

- Report the number of learners who scored 70 or more, as a distinction band.
- Print the average of the passing scores only, not of all of them.
- Change the pass mark to 50 and predict which numbers move before you run it.
