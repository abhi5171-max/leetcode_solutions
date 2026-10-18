# A. ASCII Art Contest

## Problem Statement

Three participants receive scores between 80 and 100. Determine whether the judges need to reconsider their scores.

- If the difference between the maximum and minimum scores is **at least 10**, print `check again`.
- Otherwise, print `final X`, where `X` is the median of the three scores.

## Approach

1. Read the three scores `a`, `b`, and `c`.
2. Calculate the difference between the maximum and minimum scores.
3. If the difference is at least 10, print `check again`.
4. Otherwise, sort the scores and print the middle element with the prefix `final`.

## Python Solution

```python
a, b, c = map(int, input().split())

if max(a, b, c) - min(a, b, c) >= 10:
    print("check again")
else:
    scores = sorted([a, b, c])
    print("final", scores[1])
```

## Example

**Input

```text
88 94 95
```

**Output

```text
final 94
```

**Explanation:** The difference between the maximum and minimum scores is `95 - 88 = 7`, which is less than 10. The median score is `94`.

## Complexity Analysis

- **Time Complexity:** `O(1)` — only three scores are processed.
- **Space Complexity:** `O(1)` — a fixed-size list of three scores is used.
