# A. Amusing Joke — Codeforces

## Problem Description

You are given three strings:

1. The guest's name.
2. The host's name.
3. A pile of letters found after the original letters were removed.

The letters in the pile may have been **shuffled**.

We need to determine whether the pile contains **exactly all the letters** required to form both names.

In other words:

$$
\text{letters(guest)} + \text{letters(host)} = \text{letters(pile)}
$$

The order of the letters does not matter.

---

## Approach

The simplest approach is to use **sorting**.

### Steps

1. Read the guest's name.
2. Read the host's name.
3. Read the pile of letters.
4. Concatenate the first two names.
5. Sort the combined string.
6. Sort the pile string.
7. If both sorted strings are equal, print `YES`.
8. Otherwise, print `NO`.

### Why does sorting work?

Suppose:

```text
Guest: SANTA
Host: CLAUS
```

Together:

```text
SANTACLAUS
```

If the pile is:

```text
AASLNCUAST
```

The order is different, but after sorting, both strings contain exactly the same characters.

Therefore, the pile can be rearranged to form both names.

---

## Python 3 Solution

```python
guest = input()
host = input()
pile = input()

required = guest + host

if sorted(required) == sorted(pile):
    print("YES")
else:
    print("NO")
```

---

## Example

### Input

```text
SANTACLAUS
DEDMOROZ
SANTAMOROZDEDCLAUS
```

Combine the first two names:

```text
SANTACLAUSDEDMOROZ
```

The pile contains exactly the same letters.

Therefore:

```text
YES
```

---

## Alternative Approach: Character Frequency

We can also count how many times each uppercase letter occurs.

For example:

```python
from collections import Counter

guest = input()
host = input()
pile = input()

if Counter(guest + host) == Counter(pile):
    print("YES")
else:
    print("NO")
```

This approach directly compares the frequency of every letter.

---

## Complexity

Let `N` be the total length of the strings.

Using sorting:

* **Time Complexity:** `O(N log N)`
* **Space Complexity:** `O(N)`

Since each string has a maximum length of `100`, this is easily within the limits.

---

## Key Takeaway

The important condition is:

> **The pile must contain exactly the same letters, with exactly the same frequencies, as the two names combined.**

The easiest Python solution is therefore:

```python
if sorted(guest + host) == sorted(pile):
    print("YES")
else:
    print("NO")
```
