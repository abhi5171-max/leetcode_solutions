# A. Beautiful Average

**Platform:** Codeforces  
**Language:** Python 3  
**Topic:** Arrays, Maximum Element

## Problem Statement

Given an array of length `n`, find the maximum possible average among all its contiguous subarrays.

## Approach

The maximum possible average is equal to the maximum element of the array.

A single-element subarray has an average equal to its only element. No subarray can have an average greater than the maximum element it contains.

Therefore, we can solve the problem using Python's built-in `max()` function.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a))
```

## Example

**Input

```text
3
4
3 3 3 3
5
7 1 6 9 9
5
3 4 4 4 3
```

**Output

```text
3
9
4
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case, because finding the maximum requires scanning the array.
- **Space Complexity:** `O(n)` to store the array.

## Key Learning

The problem can be solved in linear time by recognizing that a single-element subarray can achieve the maximum element's value as its average.
