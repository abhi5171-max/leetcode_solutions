# Codeforces — A. Square?

## Problem Description

Given four sticks of lengths `a`, `b`, `c`, and `d`, determine whether they can form a square without breaking or bending any stick.

A square has four equal sides and four equal interior angles.

## Approach

1. Read the number of test cases `t`.
2. For each test case, read the four stick lengths.
3. Check whether all four lengths are equal.
4. Print `YES` if they are equal; otherwise, print `NO`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    if a == b == c == d:
        print("YES")
    else:
        print("NO")
```

## Example

**Input

```text
7
1 2 3 4
1 1 1 1
2 2 2 2
1 2 1 2
1 1 5 5
5 5 5 5
4 10 5 9
```

**Output

```text
NO
YES
YES
NO
NO
YES
NO
```

## Complexity Analysis

- **Time Complexity:** `O(1)` per test case.
- **Space Complexity:** `O(1)`.

## Key Concept

Use chained equality comparisons in Python to check whether all four values are identical.

**Platform:** Codeforces  
**Problem:** A. Square?  
**Language:** Python 3
