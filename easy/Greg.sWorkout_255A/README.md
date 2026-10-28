# A. Greg's Workout

**Platform:** Codeforces  
**Problem:** [A. Greg's Workout](https://codeforces.com/problemset/problem/255/A)  
**Language:** Python 3  
**Difficulty:** 800

## Problem Description

Greg performs `n` exercises in a repeating cycle of three muscle groups: chest, biceps, and back. Each exercise is repeated a specified number of times.

Determine which muscle group receives the most training.

## Approach

1. Read `n` and the array `a`.
2. Calculate the total repetitions for each muscle group using slicing:
   - `a[0::3]` — Chest
   - `a[1::3]` — Biceps
   - `a[2::3]` — Back
3. Compare the three totals and print the muscle group with the maximum repetitions.

## Python Solution

```python
n = int(input())
a = list(map(int, input().split()))

chest = sum(a[0::3])
biceps = sum(a[1::3])
back = sum(a[2::3])

if chest > biceps and chest > back:
    print("chest")
elif biceps > chest and biceps > back:
    print("biceps")
else:
    print("back")
```

## Example

**Input

```text
7
3 3 2 7 9 6 8
```

**Output

```text
chest
```

**Explanation

- Chest: `3 + 7 + 8 = 18`
- Biceps: `3 + 9 = 12`
- Back: `2 + 6 = 8`

Chest receives the most repetitions, so the answer is `chest`.

## Complexity Analysis

- **Time Complexity:** `O(n)` — Each element is processed a constant number of times.
- **Space Complexity:** `O(n)` — The input array stores `n` integers.

## Key Concepts

- Lists and list slicing
- Summation using `sum()`
- Conditional statements
- Maximum-value comparison
