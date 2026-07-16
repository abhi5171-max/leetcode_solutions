# A. Reconnaissance 2

## Problem

Given the heights of `n` soldiers standing in a circle, find a pair of neighboring soldiers whose height difference is minimum. Since the soldiers form a circle, the first and last soldiers are also considered neighbors.

## Approach

* Read the heights of all soldiers.
* Initialize the answer with the circular pair `(n, 1)`.
* Traverse all adjacent pairs `(i, i+1)`.
* Compute the absolute height difference for each pair.
* Keep track of the pair with the minimum difference.
* Output the indices of that pair.

## Algorithm

1. Input `n` and the soldiers' heights.
2. Set the initial minimum difference using the last and first soldiers.
3. Iterate through all adjacent pairs.
4. Update the answer whenever a smaller difference is found.
5. Print the indices of the selected pair.

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

## Concepts Used

* Arrays
* Linear Traversal
* Absolute Difference
* Circular Array
