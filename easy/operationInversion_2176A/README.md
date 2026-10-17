# Codeforces - A. Operations with Inversions

## Problem

Given an array of integers, an operation allows removing an element `a[j]` if there exists an earlier element `a[i]` such that `i < j` and `a[i] > a[j]`.

The task is to determine the maximum number of operations possible.

## Approach: Greedy

1. Initialize `max_so_far` with the first array element.
2. Traverse the remaining elements.
3. If the current element is smaller than `max_so_far`, it can be removed. Increment the answer.
4. Otherwise, update `max_so_far` with the current element.
5. Print the answer for each test case.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_so_far = a[0]
    ans = 0

    for i in range(1, n):
        if a[i] < max_so_far:
            ans += 1
        else:
            max_so_far = a[i]

    print(ans)
```

## Example

**Input

```text
5
3
3 2 1
3
1 2 3
3
3 3 3
5
3 1 4 5 2
1
1
```

**Output

```text
2
0
0
2
0
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case.
- **Auxiliary Space Complexity:** `O(1)`, excluding the input array.

## Key Learning

This problem demonstrates greedy counting using a running maximum. Every element smaller than the maximum encountered before it can be removed.

**Platform:** Codeforces  
**Problem:** A. Operations with Inversions  
