# Codeforces - A. LRC and VIP

## Problem
Given an array of `n` integers, divide its elements into two non-empty sequences such that the GCD of the first sequence is different from the GCD of the second sequence.

Each element must belong to exactly one sequence.

## Approach: Greedy

The important observation is that if all array elements are equal, a valid division is impossible.

Otherwise:

1. Find the maximum element in the array.
2. Assign that maximum element to sequence `B` (label `1`).
3. Assign every other element to sequence `C` (label `2`).

Since the array is not made up of equal elements, at least one remaining element is smaller than the maximum.

Therefore:
- `gcd(B) = maximum element`
- `gcd(C) < maximum element`

Hence, the two GCDs are guaranteed to be different.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mx = max(a)

    if a.count(mx) == n:
        print("No")
    else:
        print("Yes")

        ans = [2] * n
        ans[a.index(mx)] = 1

        print(*ans)
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case.
- **Space Complexity:** `O(n)` for the output array.

## Key Concepts

- Greedy Algorithm
- Greatest Common Divisor (GCD)
- Array Traversal
- Maximum Element

## Key Takeaway

A useful greedy observation can eliminate the need to calculate GCDs for every possible partition. Isolating the maximum element gives a valid solution whenever the array contains at least two distinct values.
