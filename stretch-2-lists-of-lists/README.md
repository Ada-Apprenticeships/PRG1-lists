# Stretch 2: Lists of lists

File: `nested.py`

Optional, and a first look at something covered properly later in the module.

Each item in `register` is itself a list: a name followed by two marks.

## Predict

Three averages, then three more lines. Write them all down.

## Run

Execute and compare.

## Investigate

- `row[0]` is a name and `row[1:]` is a list of marks. Why a slice for the marks
  rather than picking them out one at a time?
- `register[0]` gives a whole row. `register[0][0]` gives one name. Read the
  second one out loud in words, left to right.
- What would `register[1][2]` give? Predict, then check.
- If a third mark were added to every learner, which lines of this program would
  need changing? That is a good test of whether it was written well.

## Modify

- Print the name of the learner with the highest average.
- Add a fourth learner and confirm nothing else needs changing.
