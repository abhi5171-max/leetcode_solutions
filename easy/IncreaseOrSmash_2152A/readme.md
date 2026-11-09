# A. Increase or Smash

## Problem Summary

Geumjae starts with an array containing only zeros.

He wants to transform it into a given target array using two operations:

1. **Increase:** Choose a positive integer and add it to every element.
2. **Smash:** Choose any subset of elements and reset them to zero.

The objective is to minimize the total number of operations.

## Approach: Mathematical Observation + Set

The important observation is that the minimum number of operations depends only on the number of distinct values in the target array.

Let `k` represent the number of distinct elements.

To construct an array with `k` distinct positive values:

- At least `k` Increase operations are required.
- At least `k - 1` Smash operations are required to separate the different groups of elements.

Therefore:

`Minimum Operations = k + (k - 1)`

Simplifying:

`Answer = 2 * k - 1`

We can efficiently count distinct elements using Python's built-in `set()` function.

## Algorithm

1. Read the number of test cases.
2. For each test case, read `n` and the target array.
3. Convert the array into a set to remove duplicates.
4. Calculate the number of distinct elements using `len()`.
5. Apply the formula `2 * distinct - 1`.
6. Print the answer.

## Python Code

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    distinct = len(set(a))

    ans = 2 * distinct - 1

    print(ans)
```

## Complexity Analysis

- **Time Complexity:** O(n) average per test case for constructing the set.
- **Space Complexity:** O(n) for storing the distinct elements.

## Key Learnings

- Python sets efficiently eliminate duplicate elements.
- Mathematical observations can simplify optimization problems.
- Greedy reasoning helps establish the minimum number of operations.
- The number of distinct values can determine the optimal answer.

## Conclusion

This problem demonstrates how identifying a mathematical pattern can replace complicated operation simulations with a simple formula.