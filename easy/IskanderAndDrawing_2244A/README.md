# README

## A. Iskander and Drawings

## Problem Statement

The page is represented by a string where:

* `#` represents one centimeter of a drawn line.
* `*` represents an empty part of the paper.

A continuous sequence of `#` characters forms a single line.

Two people erase a chosen line simultaneously from both ends:

* One person erases `1` centimeter from the left.
* The other person erases `1` centimeter from the right.

If the remaining line has a length of `1` or `2`, it is completely erased in the next second.

The goal is to find the maximum time required to erase any line.

If there are no lines, the answer is `0`.

---

## Approach

First, find the longest continuous sequence of `#` characters.

If a line has length `L`, two centimeters are erased every second. Therefore, the number of seconds required is:

```text
ceil(L / 2)
```

Using integer division, this can be written as:

```python
(L + 1) // 2
```

So, we:

1. Traverse the string.
2. Count the length of each continuous sequence of `#`.
3. Store the maximum line length.
4. Calculate `(max_length + 1) // 2`.

---

## Algorithm

For each test case:

1. Initialize `max_length = 0` and `current_length = 0`.
2. Traverse each character in the string:

   * If it is `#`, increase `current_length`.
   * Update `max_length`.
   * If it is `*`, reset `current_length` to `0`.
3. Print `(max_length + 1) // 2`.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## Example

### Input

```text
5
7
#*##*##
8
########
8
********
8
#*****##
6
*#####
```

### Output

```text
1
4
0
1
3

