# A. Cupboards

**Platform:** Codeforces  
**Problem Link:**
**Language:** Python 3  
**Difficulty:** 800

## Problem Description

There are `n` cupboards, each with a left and a right door. Every door is either open (`1`) or closed (`0`).

The goal is to make all left doors have the same position and all right doors have the same position, minimizing the number of door operations.

Each operation changes one door's position and takes one second.

## Approach

1. Count the number of open left doors (`left_open`).
2. Count the number of open right doors (`right_open`).
3. Calculate the number of closed doors:
   - `left_closed = n - left_open`
   - `right_closed = n - right_open`
4. For each side, choose the smaller number of operations needed to make all doors open or all doors closed.
5. Add these minimum values to get the answer.

## Python Solution

```python
n = int(input())

left_open = 0
right_open = 0

for _ in range(n):
    l, r = map(int, input().split())
    left_open += l
    right_open += r

left_closed = n - left_open
right_closed = n - right_open

print(min(left_open, left_closed) + min(right_open, right_closed))
```

## Example

**Input

```text
5
0 1
1 0
0 1
1 1
0 1
```

**Output

```text
3
```

## Complexity Analysis

- **Time Complexity:** `O(n)` — Each cupboard is processed once.
- **Space Complexity:** `O(1)` — Only a few counter variables are used.

## Key Concepts

- Counting
- Greedy approach
- Minimum operations
- Basic arithmetic
