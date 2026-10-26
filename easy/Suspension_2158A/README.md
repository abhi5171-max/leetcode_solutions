# A. Suspension

**Platform:** Codeforces  
**Problem:** A. Suspension  
**Language:** Python 3

## Problem Statement

Given `n` players, `y` yellow cards, and `r` red cards, determine the maximum number of players who can be suspended.

A player is suspended if they receive:

- One red card, or
- Two yellow cards.

A suspended player cannot receive any additional cards.

## Approach

1. Each red card can suspend one player.
2. Every two yellow cards can suspend one player.
3. Calculate the total possible suspensions as `r + y // 2`.
4. Since there are only `n` players, the answer cannot exceed `n`.

**Formula:**

`answer = min(n, r + y // 2)`

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    y, r = map(int, input().split())

    print(min(n, r + y // 2))
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case.
- **Space Complexity:** O(1).

## Key Concepts

- Integer division
- Greedy approach
- Minimum function
- Basic arithmetic
