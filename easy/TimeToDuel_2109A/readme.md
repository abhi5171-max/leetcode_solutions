# Codeforces - A. It's Time To Duel

## Problem Statement

There are `n` players arranged in a line. Each player plays a duel against their adjacent player, resulting in exactly `n-1` duels.

Each player reports:

- `0`: They did not win any duel.
- `1`: They won at least one duel.

Determine whether at least one player must be lying.

## Approach: Greedy Observation

There are two conditions that make the reports impossible.

### Condition 1: Consecutive Zeros

If two adjacent players both report `0`, they claim that neither won their duel against each other.

However, every duel must have exactly one winner.

Therefore, at least one player must be lying.

### Condition 2: All Ones

If all players report `1`, everyone claims to have won at least one duel.

However, there are only `n-1` duels, meaning there are exactly `n-1` winners.

It is impossible for all `n` players to have won at least one duel.

Therefore, at least one player must be lying.

### Final Decision

Print `YES` if:

1. The array contains two consecutive zeros, or
2. Every element in the array is `1`.

Otherwise, print `NO`.

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if 0 in a and "00" in "".join(map(str, a)):
        print("YES")
    elif sum(a) == n:
        print("YES")
    else:
        print("NO")
```

## Example

**Input:**

```text
6
3
0 1 0
2
0 0
2
1 1
4
0 1 1 1
4
1 0 0 1
7
0 1 0 1 0 1 0
```

**Output:**

```text
NO
YES
YES
NO
YES
NO
```

## Complexity Analysis

- **Time Complexity:** O(n) per test case because we traverse the array to check the conditions.
- **Space Complexity:** O(n) for storing the input array.

## Key Learnings

- Identifying impossible configurations using mathematical observations.
- Understanding constraints in graph-like problems.
- Using adjacent element checks in arrays.
- Simplifying a problem without simulating every duel.

---

**Problem:** A. It's Time To Duel  
**Platform:** Codeforces  
**Language:** Python 3