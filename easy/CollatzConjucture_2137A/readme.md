# A. Collatz Conjecture

**Platform:** Codeforces  
**Problem:** A. Collatz Conjecture  
**Topic:** Mathematics, Number Theory  
**Language:** Python 3

## Problem Description

Given two integers `n` and `k`, we need to find any positive integer `x` such that after performing exactly `n` Collatz operations, the final value becomes `k`.

The operations are:
- If `x` is even, divide it by 2.
- If `x` is odd, multiply it by 3 and add 1.

## Approach: Mathematical Construction

Instead of simulating the Collatz sequence, we directly construct a valid initial value.

Choose:

`x = k * 2^n`

Since the initial value is divisible by `2^n`, it remains even during all `n` operations.

Each operation divides the current value by 2.

After exactly `n` operations:

`x / 2^n = k`

Therefore, the constructed value always satisfies the requirement.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    ans = k * (2 ** n)

    print(ans)
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case using Python's built-in exponentiation (with respect to the number of iterations; big-integer arithmetic depends on the output size).
- **Space Complexity:** O(1) auxiliary space, excluding the space needed for the resulting integer.

## Key Concepts Learned

1. Collatz Conjecture
2. Mathematical observation
3. Reverse construction
4. Integer exponentiation

## Conclusion

This problem demonstrates how mathematical construction can eliminate the need for direct simulation. By multiplying the target value by `2^n`, we guarantee that all `n` operations are even-number divisions and the final value is exactly `k`.