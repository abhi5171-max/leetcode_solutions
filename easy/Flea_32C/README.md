# C. Flea

## Problem

A flea can jump exactly `s` centimeters vertically or horizontally on an `n × m` board. Starting from any cell, it can make unlimited jumps without leaving the board.

Determine how many starting positions allow the flea to reach the maximum possible number of cells.

## Approach

* Cells are divided into groups based on their row and column remainders modulo `s`.
* A flea can only visit cells that share the same row remainder and column remainder as its starting cell.
* The largest reachable region is formed by choosing the residue classes containing the maximum number of rows and columns.
* Count how many cells belong to these largest residue classes.

## Algorithm

1. Compute the quotient and remainder of `n` divided by `s`.
2. Determine how many rows belong to the largest residue classes.
3. Repeat the same process for the columns.
4. Multiply the two counts to obtain the number of optimal starting positions.

## Complexity

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

## Concepts Used

* Mathematics
* Modular Arithmetic
* Observation
* Integer Division
