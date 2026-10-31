# A. Shortest Increasing Path

## Problem Description

We start at coordinate `(0, 0)` and need to reach `(x, y)`.

The movement rules are:

- The first step must be along the X-axis.
- The second step must be along the Y-axis.
- Steps continue alternating between X and Y axes.
- Every step must have a positive integer length.
- Each step must be strictly longer than the previous step.

Find the minimum number of steps required to reach the destination. If it is impossible, return `-1`.

## Approach: Mathematical Observation

Instead of trying every possible sequence of movements, we use mathematical conditions.

### Case 1: Two Steps

If `x < y`, we can reach the destination directly:

- Move `x` units along the X-axis.
- Move `y` units along the Y-axis.

Since `x < y`, the condition is satisfied.

Answer: `2`

### Case 2: Three Steps

If `y >= 2` and `x >= y + 2`, we can use:

- First step: `1` unit along X.
- Second step: `y` units along Y.
- Third step: `x - 1` units along X.

The required condition is:

`1 < y < x - 1`

Answer: `3`

### Case 3: Impossible

If neither of the above conditions is satisfied, reaching the destination is impossible.

Answer: `-1`

## Python Solution

```python
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if x < y:
        print(2)
    elif y >= 2 and x >= y + 2:
        print(3)
    else:
        print(-1)
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case.
- **Space Complexity:** O(1).

## Key Concepts

- Greedy approach
- Mathematical observations
- Coordinate geometry
- Strictly increasing sequences
- Conditional statements
