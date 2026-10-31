# A. Sublime Sequence

## Problem Description

Farmer John has an integer `n`. He creates a sequence of length `k` by alternating between `-n` and `n`, starting with `-n`.

The task is to calculate the sum of all elements in the sequence.

## Approach: Mathematical Observation

The sequence alternates between `-n` and `n`.

We can solve the problem without constructing the sequence:

1. If `k` is even, all positive and negative pairs cancel each other. The sum is `0`.
2. If `k` is odd, one extra `-n` remains. The sum is `-n`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k % 2 == 0:
        print(0)
    else:
        print(-n)
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case.
- **Space Complexity:** O(1).

## Key Learning

- Alternating sequences
- Parity (odd and even numbers)
- Mathematical optimization
- Avoiding unnecessary array construction
