# A. Dungeon Equilibrium

**Platform:** Codeforces  
**Problem:** A. Dungeon Equilibrium  
**Language:** Python 3

## Problem Description

Given an array, find the minimum number of elements to delete so that every distinct integer remaining in the array occurs the same number of times.

## Approach

1. Use `Counter` to calculate the frequency of each distinct element.
2. Find the minimum frequency, `k`.
3. For every element, retain at most `k` occurrences and delete any excess occurrences.
4. Sum all deletions and print the result.

## Python Solution

```python
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = Counter(a)
    k = min(freq.values())

    deletions = sum(count - min(count, k) for count in freq.values())

    print(deletions)
```

## Complexity Analysis

- **Time Complexity:** O(n) per test case.
- **Space Complexity:** O(n) for storing the array and frequencies.

## Key Learning

Frequency counting with Python's `Counter` simplifies array problems involving repeated elements. The goal is to retain a common positive frequency for every distinct value while minimizing deletions.
