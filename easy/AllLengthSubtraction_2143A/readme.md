# Make All Elements Zero

## Problem Description

Given a permutation of length `n`, perform exactly `n` operations.

For every integer `k` from `1` to `n`:

- Choose a contiguous subarray of length exactly `k`.
- Subtract `1` from every element in that subarray.

Determine whether it is possible to make every element equal to zero.

## Approach: Reverse Greedy

Instead of simulating operations from `1` to `n`, process them in reverse order, from `n` down to `1`.

### Algorithm

1. Start with the original permutation.
2. Iterate `k` from `n` down to `1`.
3. Find all positions containing positive elements.
4. Check whether exactly `k` positive elements exist.
5. Check whether these positions form a contiguous subarray.
6. If both conditions hold, subtract `1` from all positive elements.
7. Otherwise, the answer is `NO`.
8. If all operations are completed, the answer is `YES`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    possible = True

    for k in range(n, 0, -1):
        positions = [i for i in range(n) if p[i] > 0]

        if len(positions) != k:
            possible = False
            break

        if positions[-1] - positions[0] + 1 != k:
            possible = False
            break

        for i in positions:
            p[i] -= 1

    print("YES" if possible else "NO")
```

## Complexity Analysis

- **Time Complexity:** O(n²) per test case.
- **Space Complexity:** O(n).

## Key Concepts Learned

- Greedy Algorithm
- Reverse Simulation
- Array Manipulation
- Contiguous Subarrays
- Position Tracking

## Conclusion

This problem demonstrates how reversing the order of operations can simplify an array transformation problem. By processing the operations from largest to smallest, we can verify whether the positive elements form the required contiguous subarray at every step.

**Status:** Solved
