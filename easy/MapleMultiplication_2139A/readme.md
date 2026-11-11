# A. Maple and Multiplication

**Platform:** Codeforces  
**Problem:** A. Maple and Multiplication  
**Language:** Python 3  
**Topics:** Mathematics, Number Theory, Implementation

## Problem Summary

Maple has two positive integers `a` and `b`.

She can perform an operation by choosing any positive integer `x` and multiplying either `a` or `b` by `x`.

The objective is to make both numbers equal using the minimum number of operations.

## Approach: Mathematical Observation

The minimum number of operations depends on the relationship between the two numbers.

### Case 1: Numbers are already equal

If:

`a == b`

No operations are needed.

Answer = `0`.

### Case 2: One number is divisible by the other

If:

`a % b == 0` or `b % a == 0`

We can multiply the smaller number by the required quotient.

Answer = `1`.

### Case 3: Neither number divides the other

We can always make both numbers equal using two operations:

- Multiply `a` by `b`.
- Multiply `b` by `a`.

Both numbers become `a * b`.

Answer = `2`.

## Python Code

```python
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        print(0)
    elif a % b == 0 or b % a == 0:
        print(1)
    else:
        print(2)
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case.
- **Space Complexity:** O(1).

Only equality and divisibility checks are performed.

## Key Learnings

- Mathematical observations can eliminate unnecessary simulations.
- The modulo operator helps check divisibility.
- Sometimes the answer can be determined by considering only a few cases.
- Multiplying both numbers strategically guarantees a solution in at most two operations.

## Conclusion

This problem demonstrates how number theory and simple conditional statements can produce an efficient solution without simulating the operations.