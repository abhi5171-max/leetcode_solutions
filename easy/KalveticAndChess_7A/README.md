# ♟️ Kalevitch and Chess

## Problem Overview

Given an 8×8 chessboard containing black (`B`) and white (`W`) cells, determine the minimum number of row and column painting operations required to produce the given board. Initially, the board is completely white, and each operation paints an entire row or an entire column black.

## Approach

* Count all rows that are completely black.
* If every row is completely black, the answer is `8` (either paint all rows or all columns).
* Otherwise:

  * Paint every completely black row.
  * For the remaining rows, count the columns that still contain black cells.
  * The final answer is:

  **Full Black Rows + Required Columns**

## Algorithm

1. Read the 8×8 board.
2. Count rows containing only `B`.
3. If all 8 rows are black, print `8`.
4. Otherwise:

   * Ignore fully black rows.
   * Count columns containing at least one black cell in the remaining rows.
5. Output the sum.

## Complexity Analysis

* **Time Complexity:** `O(8²)` (constant due to fixed board size)
* **Space Complexity:** `O(1)`

## Concepts Used

* Matrix Traversal
* Greedy Observation
* Simulation

## Tags

`Codeforces` `Greedy` `Implementation` `Matrices` `Python`
