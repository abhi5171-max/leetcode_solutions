# A. Triangular Numbers

## Problem
Determine whether a given integer is a triangular number.

A triangular number is the sum of the first `n` natural numbers:

T(n) = 1 + 2 + 3 + ... + n

Examples:
- 1
- 3
- 6
- 10
- 15
- ...

## Approach
- Start with a running sum of `0`.
- Add consecutive integers starting from `1`.
- Stop when the sum becomes greater than or equal to the given number.
- If the final sum equals the given number, print `YES`; otherwise, print `NO`.

## Algorithm
1. Read the integer `n`.
2. Initialize:
   - `sum = 0`
   - `i = 1`
3. While `sum < n`:
   - Add `i` to `sum`.
   - Increment `i`.
4. Compare `sum` with `n`.
5. Print:
   - `YES` if equal.
   - `NO` otherwise.

## Complexity
- **Time:** O(√n)
- **Space:** O(1)

## Concepts Used
- Loops
- Simulation
- Mathematical Sequences