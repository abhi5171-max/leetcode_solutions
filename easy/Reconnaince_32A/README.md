# A. Reconnaissance

## Problem
Given the heights of `n` soldiers and a maximum allowed height difference `d`, determine the number of **ordered pairs** of soldiers that can form a reconnaissance unit. Two soldiers can form a unit if the absolute difference between their heights is at most `d`.

Since `(i, j)` and `(j, i)` are considered different, both pairs must be counted.

## Approach
- Read the number of soldiers and the maximum allowed height difference.
- Compare every pair of soldiers using two nested loops.
- Skip pairs where both indices are the same.
- If the height difference is less than or equal to `d`, increment the answer.
- Print the final count.

## Algorithm
1. Read `n` and `d`.
2. Read the soldiers' heights.
3. Initialize `count = 0`.
4. For every pair `(i, j)`:
   - If `i != j` and `abs(height[i] - height[j]) <= d`, increment `count`.
5. Output `count`.

## Complexity Analysis
- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(1)`

## Python Solution
```python
n, d = map(int, input().split())
heights = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(n):
        if i != j and abs(heights[i] - heights[j]) <= d:
            count += 1

print(count)
```

## Example

### Input
```
5 10
10 20 50 60 65
```

### Output
```
6
```

## Key Concepts
- Brute Force
- Nested Loops
- Array Traversal
- Ordered Pairs