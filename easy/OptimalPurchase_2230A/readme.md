# A. Optimal Purchase

**Platform:** Codeforces  
**Problem:** A. Optimal Purchase  
**Topic:** Greedy, Mathematics  
**Language:** Python 3

## Problem Description

We are given `n` students who need access to an online course.

There are two types of keys:

- Individual key: Costs `a` dollars and provides access to one student.
- Group key: Costs `b` dollars and provides access to up to three students.

The task is to calculate the minimum cost required to provide access to all students.

## Approach: Greedy

First, compare the cost of three individual keys with one group key.

`3 * a` versus `b`

- If `b >= 3 * a`, individual keys are cheaper or equally expensive.
- Otherwise, group keys are cheaper for every complete group of three.

Calculate:

- Complete groups: `n // 3`
- Remaining students: `n % 3`

The minimum cost is:

`(n // 3) * b + min((n % 3) * a, b)`

If individual keys are cheaper than group keys for three students, simply purchase all individual keys.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if b >= 3 * a:
        ans = n * a
    else:
        ans = (n // 3) * b + min((n % 3) * a, b)

    print(ans)
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case.
- **Space Complexity:** O(1).

## Key Concepts Learned

1. Greedy algorithms
2. Mathematical comparison
3. Integer division (`//`)
4. Modulo operator (`%`)
5. Cost optimization

## Conclusion

This problem demonstrates how comparing the cost of different purchasing options can lead to an optimal greedy solution without requiring simulation or dynamic programming.