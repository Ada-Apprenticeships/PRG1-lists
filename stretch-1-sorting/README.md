# Stretch 1: Sorting

File: `sorting.py`

Optional. Only if you have finished the four core activities.

## Predict

Five lines of output. Write them all down, and pay attention to the third one.

## Run

Execute and compare.

## Investigate

- The third line prints `scores` after two `sorted()` calls, and it is unchanged.
  Why?
- In the songs block, the first sort puts every capitalised title before every
  lowercase one. What is it actually comparing, if not the letters as a person
  reads them?
- `key=str.lower` fixes it. Describe in one sentence what `key` is doing, without
  using the word "key".

## Modify

- Sort the songs by length rather than alphabetically.
- Sort the scores so the highest is first, without using `reverse=True`.
