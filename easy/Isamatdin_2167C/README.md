# C. Isamatdin and His Magic Wand

**Platform:** Codeforces  
**Problem:** C. Isamatdin and His Magic Wand!  
**Language:** Python 3  
**Difficulty:** Competitive Programming

## Problem Description

Given an array of integers, we can swap two elements only when one is even and the other is odd. The goal is to obtain the lexicographically smallest possible arrangement.

## Approach

1. Check whether the array contains at least one even number and at least one odd number.
2. If both parities exist, sort the array in ascending order.
3. Otherwise, leave the array unchanged because no valid swap is possible.
4. Print the resulting array.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    has_even = any(x % 2 == 0 for x in a)
    has_odd = any(x % 2 != 0 for x in a)

    if has_even and has_odd:
        a.sort()

    print(*a)
```

## Complexity Analysis

- **Time Complexity:** O(n log n) per test case when sorting is possible.
- **Space Complexity:** O(n) for storing the array.

## Key Learning

The problem demonstrates how identifying an operation's constraints can simplify a sorting problem. When both even and odd elements exist, valid swaps allow any pair of elements to exchange positions through a sequence of operations. When all elements have the same parity, the array cannot change.
