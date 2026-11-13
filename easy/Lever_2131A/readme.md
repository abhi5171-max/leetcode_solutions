# Codeforces 2131A - A. Lever

## Problem Explanation

You are given two arrays `a` and `b` of length `n`.

In each iteration:
- If an element `a[i] > b[i]` exists, decrease one such element by 1.
- If an element `a[i] < b[i]` exists, increase one such element by 1.
- If no element satisfies `a[i] > b[i]`, the process stops after that iteration.

Find the total number of iterations.

## Approach

1. Calculate the positive differences between corresponding elements of `a` and `b`.
2. Add all positive differences.
3. Add 1 for the final iteration in which no decrease is possible.
4. Print the result.

**Formula:**

`Answer = 1 + sum(max(0, a[i] - b[i]))`

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 1 + sum(max(0, a[i] - b[i]) for i in range(n))

    print(ans)
```

## Example

**Input:**
```text
4
2
7 3
5 6
3
3 1 4
3 1 4
1
10
1
6
1 1 4 5 1 4
1 9 1 9 8 1
```

**Output:**
```text
3
1
10
7
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case, because we traverse both arrays once.
- **Space Complexity:** `O(n)` for storing the two arrays.

## Key Learning

- Calculating positive differences between two arrays.
- Using `max(0, difference)` to ignore negative values.
- Identifying the extra final iteration in a simulation problem.
- Converting a simulation into a simple mathematical formula.

---

**Status:** Accepted solution logic  
**Problem:** Codeforces 2131A - A. Lever