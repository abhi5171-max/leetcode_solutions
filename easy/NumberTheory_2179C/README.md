# C. Blackslex and Number Theory

**Platform:** Codeforces  
**Problem:** C. Blackslex and Number Theory  
**Language:** Python 3  
**Topic:** Number Theory, Greedy, Sorting

## Problem Summary

Given an array of distinct positive integers, we can repeatedly replace an element `a[i]` with `a[i] % x`, where `x >= k`. The objective is to find the maximum positive integer `k` for which all array elements can be made equal.

## Approach

1. Sort the array in ascending order.
2. Identify the smallest element `a[0]` and the second-smallest element `a[1]`.
3. Calculate the maximum possible value of `k` using:

   `answer = max(a[0], a[1] - a[0])`

4. Print the answer for each test case.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    print(max(a[0], a[1] - a[0]))
```

## Example

**Input

```text
3
3
5 7 9
2
2 3
7
11 74 5 22 52 97 82
```

**Output

```text
5
2
6
```

## Complexity Analysis

- **Time Complexity:** `O(n log n)` per test case.
- **Space Complexity:** `O(n)` for storing the array.

## Key Learning

The problem demonstrates how sorting and examining the two smallest elements can reduce a number-theory problem to a simple mathematical expression.
