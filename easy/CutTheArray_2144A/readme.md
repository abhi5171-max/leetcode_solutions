# A. Cut the Array

**Platform:** Codeforces  
**Problem:** A. Cut the Array  
**Language:** Python 3  
**Topic:** Brute Force, Prefix Sum, Modular Arithmetic

## Problem Description

Given an array of `n` non-negative integers, divide it into three non-empty contiguous parts:

1. Prefix: Elements from index `1` to `l`.
2. Middle: Elements from index `l+1` to `r`.
3. Suffix: Elements from index `r+1` to `n`.

Calculate the sum of each part modulo `3`.

A valid partition must satisfy either:

- All three remainders are equal.
- All three remainders are pairwise different.

If a valid partition exists, print its boundaries `l` and `r`. Otherwise, print `0 0`.

## Approach: Brute Force

- Use two nested loops to explore every possible pair of partition boundaries.
- Calculate the sum of each of the three segments modulo `3`.
- Check whether all three remainders are equal or all are different.
- Print the first valid partition.
- If no valid partition exists, print `0 0`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    found = False

    for l in range(1, n - 1):
        for r in range(l + 1, n):

            s1 = sum(a[:l]) % 3
            s2 = sum(a[l:r]) % 3
            s3 = sum(a[r:]) % 3

            if (s1 == s2 == s3) or (len({s1, s2, s3}) == 3):
                print(l, r)
                found = True
                break

        if found:
            break

    if not found:
        print(0, 0)
```

## Complexity Analysis

- **Time Complexity:** O(n³)
- **Space Complexity:** O(n)

## Key Concepts Learned

- Brute Force
- Array Partitioning
- Modular Arithmetic
- Nested Loops
- Set Operations in Python

## Conclusion

This problem demonstrates how to explore possible array partitions and use modular arithmetic to validate conditions efficiently for small constraints.

---

**Status:** Solved
