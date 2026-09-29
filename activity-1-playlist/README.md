# Activity 1: The playlist

File: `playlist.py`

A music queue: songs get added, played, skipped ahead of and pulled out.

## Predict

Write down every line of output before running. There are nine. The last one is
the whole list, so get the order right as well as the contents.

## Run

Execute it.

## Investigate

- `playlist[0]` and `playlist[-1]` picked out the first and last songs. That is
  the same notation you used on strings yesterday. What does that tell you about
  how Python thinks about both?
- `pop(0)` did two things at once. Name both.
- `insert(1, "Golden Hour")` put a song at position 1. What happened to the song
  that was already there?
- The `remove` is inside an `if`. What would happen without the `if`, if the song
  were not in the list? Predict first, then try it.

## Modify

- Add a song to the end of the queue without using `append`.
- Play the next two songs in one go, printing both titles.
- Change the program so removing a song that is not there prints a message
  rather than doing nothing.
