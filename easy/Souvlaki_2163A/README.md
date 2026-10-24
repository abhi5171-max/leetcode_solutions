# Codeforces 2163A — Souvlaki VS. Kalamaki

**Problem:** [A. Souvlaki VS. Kalamaki](https://codeforces.com/problemset/problem/2163/A)

**Language:** Python 3

**Topics:** Sorting, Greedy, Game Theory

## Problem Statement

Two players play a game on an array of `n` integers. Souvlaki plays on odd-numbered rounds, and Kalamaki plays on even-numbered rounds. Each player can either skip their turn or swap the two adjacent elements corresponding to that round.

Before the game begins, Souvlaki can rearrange the array. Determine whether he can guarantee that the array is sorted in non-decreasing order at the end of the game.

## Approach

1. Sort the array in non-decreasing order.
2. Check adjacent pairs starting from index `1`, advancing by `2`.
3. If `a[i] != a[i + 1]` for any checked pair, print `NO`.
4. Otherwise, print `YES`.

## Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    possible = True

    for i in range(1, n - 1, 2):
        if a[i] != a[i + 1]:
            possible = False
            break

    print("YES" if possible else "NO")
```

## Complexity Analysis

- **Time Complexity:** `O(n log n)` per test case due to sorting.
- **Space Complexity:** `O(n)` for storing the array.

## Example

**Input

```text
5
4
4 2 2 1
4
1 1 1 1
5
1 5 1 5 1
3
1 2 3
5
1 3 2 3 5
```

**Output

```text
YES
YES
YES
NO
NO
```

## Key Learning

Sorting can reveal the structure required for a winning strategy. Checking alternating adjacent pairs is sufficient to determine whether Souvlaki can guarantee victory.
