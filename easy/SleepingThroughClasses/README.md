# Codeforces - A. Sleeping Through Classes

## Problem Statement

Given `n` classes represented by a binary string `s`, where `1` represents an important class and `0` represents a non-important class, find the maximum number of classes you can sleep through.

After attending an important class at index `i`, you must stay awake for the next `k` classes.

## Approach

1. Initialize `sleep = 0` to count the classes we can sleep through.
2. Initialize `awake_until = -1` to track the last class during which we must stay awake.
3. Iterate through every class:
   - If `s[i] == '1'`, update `awake_until = i + k`.
   - Otherwise, if `i > awake_until`, increment `sleep`.
4. Print the total number of classes we can sleep through.

## Python Code

```python
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    sleep = 0
    awake_until = -1

    for i in range(n):
        if s[i] == '1':
            awake_until = i + k
        elif i > awake_until:
            sleep += 1

    print(sleep)
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case, because we traverse the string once.
- **Space Complexity:** `O(1)` auxiliary space, excluding the input string.

## Key Concept

Track the last class until which you must remain awake. A class represented by `0` can be counted as sleep only when its index is beyond that boundary.
