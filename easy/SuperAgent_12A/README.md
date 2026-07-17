# A. Super Agent

## Problem Description

Given a **3 × 3** keypad where:

- `X` represents a pressed button.
- `.` represents an unpressed button.

Determine whether the pattern is **centrally symmetric** about the center button.

Print:

- `YES` if it is symmetric.
- `NO` otherwise.

---

## Approach

For central symmetry, every cell `(i, j)` must match its opposite cell:

```
(2 - i, 2 - j)
```

Check all nine positions:

- If any pair differs, the pattern is not symmetric.
- Otherwise, it is symmetric.

---

## Algorithm

1. Read the 3×3 grid.
2. Traverse every cell.
3. Compare each cell with its centrally opposite cell.
4. If any mismatch is found, print `NO`.
5. Otherwise, print `YES`.

---

## Correctness

A figure is centrally symmetric if every point has an identical counterpart after a 180° rotation about the center.

The algorithm verifies this property by comparing every cell with its opposite position.

If every comparison matches, the grid satisfies central symmetry; otherwise, it does not.

---

## Complexity Analysis

- **Time Complexity:** `O(1)` (only 9 cells are checked)
- **Space Complexity:** `O(1)`

---

## Concepts Used

- Matrix Traversal
- Simulation
- Coordinate Transformation
- Symmetry Checking