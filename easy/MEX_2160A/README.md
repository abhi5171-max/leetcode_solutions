# 2160A. MEX Partition

- **Platform:** Codeforces
- **Problem:** [A. MEX Partition](https://codeforces.com/problemset/problem/2160/A)
- **Language:** Python 3
- **Difficulty:** 800

## Problem Statement

Given a multiset of integers, find the minimum possible score among all valid partitions, where every multiset in a partition has the same MEX.

## Approach

1. Create a frequency array to count the occurrences of each integer.
2. Iterate through integers starting from `0`.
3. Find the first integer whose frequency is less than `2`.
4. Print that integer as the answer.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * 102

    for x in a:
        freq[x] += 1

    for i in range(102):
        if freq[i] < 2:
            print(i)
            break
```

## Complexity Analysis

- **Time Complexity:** O(n + 101), effectively O(n).
- **Space Complexity:** O(1), since the frequency array has a fixed size.

## Key Concepts

- MEX (Minimum Excluded Value)
- Frequency counting
- Greedy / Mathematical observation
