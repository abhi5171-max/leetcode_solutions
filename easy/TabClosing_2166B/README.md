# Codeforces B. Tab Closing

## Problem Description

You are given a screen of length `a`, containing `b` tabs. Each tab has a dynamically changing length, and you must close all tabs by clicking the `x` at the right endpoint of each tab.

The goal is to find the minimum number of mouse moves required to close all tabs.

## Approach

The tab width changes as tabs are closed. The minimum number of mouse moves is either `1` or `2`.

- If `a / c == b`, print `1`.
- Otherwise, print `2`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    if a // c == b:
        print(1)
    else:
        print(2)
```

## Example

**Input

```text
12
8 1 6
9 6 2
10 3 1
10 1 10
9 2 1
5 5 6
6 2 7
9 1 9
3 2 6
8 1 7
8 1 9
8 2 4
```

**Output

```text
1
2
1
1
1
1
2
1
2
1
2
1
```

## Complexity Analysis

- **Time Complexity:** `O(1)` per test case.
- **Space Complexity:** `O(1)`.

## Key Concept

Analyze how tab widths change as tabs are closed to minimize cursor movement.

**Platform:** Codeforces  
**Problem:** B. Tab Closing  
**Language:** Python 3
