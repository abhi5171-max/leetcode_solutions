# A. Little Fairy's Painting

**Platform:** Codeforces  
**Language:** Python 3  
**Topic:** Sets, Simulation, Implementation

## Problem Description

A ribbon contains \(10^{18}\) cells. The first \(n\) cells are already colored. For each remaining cell, the fairy counts the number of distinct colors currently present and uses that number as the new cell's color.

Find the color used for the last cell.

## Approach

1. Store the initial colors in a set to obtain distinct colors.
2. Let `k` be the number of distinct colors.
3. If `k` is already present, the color count remains unchanged, so the answer is `k`.
4. Otherwise, add `k` as a new color and update the distinct-color count.
5. Repeat until the count stabilizes, then print it.

## Complexity Analysis

- **Time Complexity:** \(O(n)\) expected per test case.
- **Space Complexity:** \(O(n)\).

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    colors = set(a)
    k = len(colors)

    while k not in colors:
        colors.add(k)
        k = len(colors)

    print(k)
```

## Key Learning

A set efficiently tracks distinct colors. Once the current number of distinct colors is itself present in the set, adding further cells cannot introduce a new color, and the process stabilizes.
