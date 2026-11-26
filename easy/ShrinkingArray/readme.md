# Codeforces - B. Shrinking Array

## Problem

Given an integer array, we can repeatedly choose two adjacent elements and replace them with an integer between their minimum and maximum values.

An array is called beautiful if:
- It contains at least two elements.
- At least one adjacent pair has an absolute difference of at most 1.

Find the minimum number of operations required to make the array beautiful, or print `-1` if it is impossible.

## Approach: Greedy + Local Extrema

There are three cases:

### Case 1: The array is already beautiful

Check every adjacent pair:

```python
abs(a[i] - a[i + 1]) <= 1
```

If any pair satisfies the condition, the answer is `0`.

### Case 2: A local maximum or minimum exists

A local maximum satisfies:

```python
a[i] > a[i - 1] and a[i] > a[i + 1]
```

A local minimum satisfies:

```python
a[i] < a[i - 1] and a[i] < a[i + 1]
```

If either exists, we can merge an adjacent pair and select a replacement value that makes it close to the other neighbor.

Therefore, the answer is `1`.

### Case 3: No local extrema exist

If the array is not already beautiful and contains no local maximum or minimum, it must be strictly increasing or strictly decreasing.

In this situation, making the array beautiful is impossible.

Therefore, the answer is `-1`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    beautiful = False

    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) <= 1:
            beautiful = True
            break

    if beautiful:
        print(0)
        continue

    possible = False

    for i in range(1, n - 1):
        if (a[i] > a[i - 1] and a[i] > a[i + 1]) or \
           (a[i] < a[i - 1] and a[i] < a[i + 1]):
            possible = True
            break

    if possible:
        print(1)
    else:
        print(-1)
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case.
- **Space Complexity:** `O(1)` auxiliary space.

## Key Concepts

- Greedy Algorithm
- Array Traversal
- Adjacent Elements
- Local Maximum and Minimum
- Absolute Difference

## Key Takeaway

First check whether the required condition is already satisfied. If not, look for a local maximum or minimum. Recognizing this pattern helps determine whether one operation is sufficient or the answer is impossible.
