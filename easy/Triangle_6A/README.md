# A. Triangle

## Problem Statement
Given four stick lengths, determine whether any three of them can form:

- A **non-degenerate triangle** (`TRIANGLE`)
- A **degenerate triangle** (`SEGMENT`)
- Or if forming any triangle is **impossible** (`IMPOSSIBLE`)

A valid triangle must satisfy the triangle inequality.

## Approach
Since there are only **4 sticks**, we can check every possible combination of **3 sticks**.

For each combination:
1. Sort the three stick lengths.
2. If `a + b > c`, a valid triangle exists.
3. If `a + b == c`, a degenerate triangle exists.
4. Otherwise, the combination cannot form a triangle.

If at least one valid triangle is found, output `TRIANGLE`.
Otherwise, if a degenerate triangle exists, output `SEGMENT`.
If neither exists, output `IMPOSSIBLE`.

## Algorithm
1. Read the four stick lengths.
2. Generate all four possible groups of three sticks.
3. Sort each group.
4. Check:
   - `a + b > c` → `TRIANGLE`
   - `a + b == c` → remember `SEGMENT`
5. After checking all combinations:
   - Print `SEGMENT` if possible.
   - Otherwise print `IMPOSSIBLE`.

## Correctness
The algorithm examines every possible set of three sticks exactly once.
Since every possible triangle is evaluated using the triangle inequality, the result is always correct.

## Complexity Analysis
- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

## Concepts Used
- Brute Force
- Sorting
- Triangle Inequality
- Conditional Logic