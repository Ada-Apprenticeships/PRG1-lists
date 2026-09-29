# Activity 3: In place, or a new one?

File: `in_place_or_new.py`

The most important thing to know about lists, and the thing that makes them
behave unlike the strings you met yesterday.

## Predict

Three blocks separated by dashes. Eight lines of output in total. Write them all
down first, and be careful with the ones that print `result`.

## Run

Execute and compare.

## Investigate

- `playlist.append("Flowers")` was assigned to `result`, and `result` printed as
  `None`. Yet the playlist did change. What does that tell you about what
  `append` hands back?
- `sorted(playlist)` gave a sorted list **and** left the original alone. Compare
  that with `.sort()` in the third block, which did the opposite. Write the
  difference down in one sentence each.
- Yesterday you learned that a string method never changes the string it was
  called on. Lists are the other way round: a list method usually changes the
  list and hands back nothing. Why does it matter that these two behave in
  opposite ways?

## Modify

- Rewrite the third block so the sorted playlist ends up in a new variable and
  the original order is preserved.
- Make `alphabetical` sort in reverse order without changing `playlist`.

> `result = playlist.append(song)` is a fault almost everyone writes once. It
> quietly replaces your playlist with nothing. You will meet it again in about
> ten minutes.
