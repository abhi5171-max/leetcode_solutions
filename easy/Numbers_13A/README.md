# A. Numbers

## Problem Description

Given an integer **A**, compute the average value of the sum of digits of **A** when written in every base from **2** to **A − 1**.

The answer must be printed as an **irreducible fraction** in the form `X/Y`.

---

## Approach

For every base from **2** to **A − 1**:

1. Convert the number **A** into that base.
2. Calculate the sum of its digits using repeated division and modulo operations.
3. Add the digit sum to a running total.

After processing all bases:

- The denominator is `A - 2` (total number of bases).
- Reduce the fraction using the Greatest Common Divisor (GCD).

---

## Algorithm

1. Read integer `A`.
2. Initialize `total = 0`.
3. For every base `b` from `2` to `A-1`:
   - Repeatedly extract digits using `% b`.
   - Add each digit to `total`.
4. Compute `gcd(total, A-2)`.
5. Print the reduced fraction.

---

## Correctness

The algorithm correctly computes the digit sum in every valid base by repeatedly extracting the least significant digit (`A % base`) and removing it (`A //= base`).

Since every base from **2** to **A−1** is processed exactly once, the total digit sum is correct.

Dividing by the total number of bases gives the required average, and reducing it with GCD produces the irreducible fraction.

---

## Complexity Analysis

- **Time Complexity:** `O(A log A)`
- **Space Complexity:** `O(1)`

---

## Concepts Used

- Number Base Conversion
- Modulo Arithmetic
- Greatest Common Divisor (GCD)
- Simulation