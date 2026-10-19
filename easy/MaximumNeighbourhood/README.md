# A. Maximum Neighborhood

**Platform:** Codeforces  
**Problem:** Maximum Neighborhood  
**Language:** Python 3

## Problem Description

Given an \(n \times n\) grid filled with consecutive integers from \(1\) to \(n^2\), find the maximum cost of any cell.

The cost of a cell is the sum of its own value and the values of its side-adjacent neighbors (up, down, left, and right).

## Approach

The grid values increase from left to right and from top to bottom. The maximum cost can be calculated directly using a mathematical formula.

- If \(n = 1\), the only cell has cost `1`.
- If \(n = 2\), the maximum cost is `9`.
- If \(n \ge 3\), the maximum cost is `4 * n * n - 3 * n - 1`.

This avoids constructing the grid and checking every cell.

## Complexity Analysis

- **Time Complexity:** \(O(1)\) per test case.
- **Space Complexity:** \(O(1)\).

## Example

**Input

```text
5
1
2
3
4
5
```

**Output

```text
1
9
29
56
95
```

## Key Learning

This problem demonstrates how to replace grid simulation with a mathematical formula to achieve constant-time computation.
