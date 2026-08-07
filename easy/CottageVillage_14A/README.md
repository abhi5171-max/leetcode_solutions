# 🏡 Cottage Village

## Problem
A village contains square houses centered on the x-axis. A new square house of side length `t` must:
- Be centered on the x-axis.
- Touch at least one existing house.
- Not overlap any existing house.

Determine the number of possible positions for the new house.

## Approach
- Sort all houses by their x-coordinate.
- There are always two possible positions:
  - Before the first house.
  - After the last house.
- For every pair of adjacent houses:
  - Compute the empty gap between their boundaries.
  - If the gap equals `t`, exactly **one** position exists.
  - If the gap is greater than `t`, **two** positions exist.
  - Otherwise, no additional position exists.

## Algorithm
1. Read all houses.
2. Sort by center position.
3. Initialize answer as `2`.
4. For every adjacent pair:
   - Calculate available gap.
   - Update the answer based on the gap size.
5. Print the result.

## Complexity
- **Time:** `O(n log n)` (sorting)
- **Space:** `O(n)`

## Concepts Used
- Sorting
- Geometry
- Greedy
- Interval Gap Analysis