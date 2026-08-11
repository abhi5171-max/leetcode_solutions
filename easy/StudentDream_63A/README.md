# A. A Student's Dream

## Problem

A Venusian girl and a Martian boy want to hold hands comfortably.

The girl has:

* `al` fingers on her left hand
* `ar` fingers on her right hand

The boy has:

* `bl` fingers on his left hand
* `br` fingers on his right hand

For the hands that are holding each other:

1. Between every two girl's fingers, there must be a boy's finger.
2. No three fingers of the boy can be next to each other.

The boy and girl can stand in either orientation, so both possible hand combinations must be checked.

## Key Observation

Suppose the girl has `G` fingers and the boy has `B` fingers in the two hands that are touching.

### Condition 1: Separate the girl's fingers

Between every two girl's fingers, there must be at least one boy's finger.

Therefore:

```text
B >= G - 1
```

### Condition 2: No three boy fingers together

Boy fingers can appear in groups of at most two.

There are `G + 1` possible gaps around the girl's fingers:

```text
_ G _ G _ G _ ...
```

Each gap can contain at most two boy fingers.

Therefore:

```text
B <= 2 * (G + 1)
```

or:

```text
B <= 2G + 2
```

Thus, the two hands can hold each other if:

```text
G - 1 <= B <= 2G + 2
```

## Two Possible Orientations

### Boy on the left

The girl's left hand touches the boy's right hand:

```text
Girl Left  ↔  Boy Right
```

So we check:

```text
al - 1 <= br <= 2 * al + 2
```

### Boy on the right

The girl's right hand touches the boy's left hand:

```text
Girl Right  ↔  Boy Left
```

So we check:

```text
ar - 1 <= bl <= 2 * ar + 2
```

If either orientation is possible, the answer is `YES`.

## Algorithm

```text
Read al, ar
Read bl, br

if (al - 1 <= br <= 2*al + 2):
    print YES

else if (ar - 1 <= bl <= 2*ar + 2):
    print YES

else:
    print NO
```

## Python 3 Solution

```python
def possible(g, b):
    return g - 1 <= b <= 2 * g + 2


gl, gr = map(int, input().split())
bl, br = map(int, input().split())

# Boy is on the left:
# Girl's left hand touches Boy's right hand
if possible(gl, br):
    print("YES")

# Boy is on the right:
# Girl's right hand touches Boy's left hand
elif possible(gr, bl):
    print("YES")

else:
    print("NO")
```

## Complexity

Only a constant number of comparisons are performed.

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

## Example

### Input

```text
5 1
10 5
```

Consider the first orientation:

```text
Girl Left = 5
Boy Right = 5
```

Check:

```text
5 - 1 <= 5 <= 2 * 5 + 2
4 <= 5 <= 12
```

The condition is satisfied, so:

```text
YES
```

## Key Concept

The problem reduces to finding the valid range of boy fingers for a given number of girl fingers:

```text
G - 1 <= B <= 2G + 2
```

Then simply test both possible orientations.

## Tags

`Greedy` `Math` `Implementation` `Combinatorics` `Codeforces`
