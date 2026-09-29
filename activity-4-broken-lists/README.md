# Activity 4: Broken lists

File: `broken_lists.py`

Three faults. Nothing crashes, and every output looks like it could be right
until you check it properly.

## Predict

Work out what each call **should** produce:

- Adding "Golden Hour" to a two song queue
- Removing both flagged songs, "Espresso" and "Flowers", from a four song list
- Backing up a list, then adding to the original

## Run

Execute it. All three are wrong.

## Investigate

- `add_song` printed `None`. Activity 3 covered exactly why. What did the author
  assume `append` handed back?
- `remove_flagged` removed "Espresso" but left "Flowers" behind. Trace the loop
  by hand, writing down the list and the current position after each pass. The
  list gets shorter while the loop is walking through it, and something gets
  skipped. Work out which and why.
- `make_backup` looks harmless. After appending to `original`, the backup has
  changed too. What did `backup = playlist` actually copy?

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. You should get a three song queue, a list with both flagged songs
gone, and a backup that does not change when the original does.

> The second fault is the nastiest thing in this module so far. Removing items
> from a list while looping over it is legal, runs without complaint, and
> silently skips things. The fix is to loop over a copy, or to build a new list
> of what you want to keep.
