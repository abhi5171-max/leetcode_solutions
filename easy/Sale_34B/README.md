# 📺 Sale

## Problem

Bob can carry at most `m` TV sets. Some TVs have negative prices, meaning Bob earns money by taking them. Determine the maximum amount of money Bob can earn.

## Approach

1. Sort all TV prices in ascending order.
2. Negative prices appear first after sorting.
3. Pick up to `m` negative-priced TVs.
4. Add the absolute value of each selected negative price to the answer.
5. Stop once a non-negative price is encountered.

## Algorithm

* Read `n`, `m`, and the list of prices.
* Sort the prices.
* Traverse the first `m` elements.
* If a price is negative, add its absolute value to the answer.
* Output the final earnings.

## Complexity Analysis

* **Time Complexity:** `O(n log n)` (sorting)
* **Space Complexity:** `O(1)` (excluding sorting overhead)

## Concepts Used

* Sorting
* Greedy Algorithm
* Array Traversal
