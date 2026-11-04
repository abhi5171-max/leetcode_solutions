# A. Same Difference

## Problem Description

Given a string consisting of lowercase English letters, we can perform the following operation:

Choose an index `i` and change `s[i]` into `s[i+1]`.

The objective is to make all characters in the string identical using the minimum number of operations.

## Approach: Greedy

The optimal strategy is to make every character equal to the last character of the string.

**Key Observation:**
- The last character cannot be changed because there is no character after it.
- Every character different from the last character must be changed at least once.
- We can process the string from right to left, changing each differing character into its right neighbor.
- Therefore, the minimum number of operations equals the number of characters different from the last character.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = 0

    for i in range(n):
        if s[i] != s[-1]:
            ans += 1

    print(ans)
```

## Complexity Analysis

- **Time Complexity:** O(n) per test case.
- **Space Complexity:** O(1).

## Key Concepts Learned

1. Greedy algorithm
2. String traversal
3. Character comparison
4. Optimal target selection

## Conclusion

This problem demonstrates how choosing the correct target character simplifies a greedy problem. By selecting the last character as the target, we can calculate the minimum operations with a single traversal of the string.