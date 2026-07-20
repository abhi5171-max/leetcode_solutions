# 🎲 Die Roll

## Problem

Given the results of Yakko's (`Y`) and Wakko's (`W`) dice rolls, determine the probability that Dot can roll a number **greater than or equal to** the maximum of the two values and win. If Dot ties with the highest roll, she still wins.

## Approach

1. Find the maximum of `Y` and `W`.
2. Count the favorable outcomes from that value to `6`.
3. Total possible outcomes are always `6`.
4. Reduce the resulting fraction using the Greatest Common Divisor (GCD).

## Algorithm

* Read `Y` and `W`.
* Compute `max_roll = max(Y, W)`.
* Calculate `favorable = 7 - max_roll`.
* Simplify `favorable / 6` using GCD.
* Print the reduced fraction.

## Complexity Analysis

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

## Concepts Used

* Probability
* Greatest Common Divisor (GCD)
* Basic Mathematics
