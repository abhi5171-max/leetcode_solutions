# A. Tatar TV Show

**Platform:** Codeforces  
**Problem:** A. Tatar TV Show  
**Topic:** Strings, Mathematics, Parity, Graph Theory  
**Language:** Python 3

## Problem Description

Given a binary string `s` of length `n` and an integer `k`, we can perform the following operation any number of times:

Choose an index `i` such that `1 <= i <= n-k` and invert the characters at positions `i` and `i+k`.

The objective is to determine whether we can make the entire string equal to zero.

## Approach: Parity Checking

The operation only connects positions separated by exactly `k`.

Therefore, positions can be divided into `k` independent groups based on their indices modulo `k`.

**Key Observation:**

- Every operation flips exactly two bits.
- The parity of the number of ones in each group remains unchanged.
- A group can become entirely zero if and only if it initially contains an even number of ones.
- Therefore, every group must have an even number of ones.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    count = [0] * k

    for i in range(n):
        if s[i] == '1':
            count[i % k] += 1

    if all(x % 2 == 0 for x in count):
        print("YES")
    else:
        print("NO")
```

## Complexity Analysis

- **Time Complexity:** O(n) per test case.
- **Space Complexity:** O(k) per test case.

## Key Concepts Learned

1. Binary string manipulation
2. Modular arithmetic
3. Parity checking
4. Graph connectivity
5. Mathematical observations

## Conclusion

This problem demonstrates how identifying independent groups and using parity invariants can eliminate the need for simulating operations.

Instead of trying every possible sequence of moves, we only need to check whether each group contains an even number of ones.