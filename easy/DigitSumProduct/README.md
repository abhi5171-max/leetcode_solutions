📄 README – Digit Sum Product
# Digit Sum Product

## Problem Statement

Given an integer `n`, create a new integer `x` by concatenating all the non-zero digits of `n` while preserving their original order.

Compute the sum of the digits in `x`, then return:

x × (sum of digits)

If `n` contains no non-zero digits, then `x = 0`.

---

## Examples

### Example 1

Input:

n = 10203004


Output:

12340


Explanation:
- x = 1234
- Sum = 1 + 2 + 3 + 4 = 10
- Answer = 1234 × 10 = 12340

### Example 2

Input:

n = 1000


Output:

1


---

## Approach

- Traverse each digit of the number.
- Ignore zeros.
- Build the new number `x`.
- Simultaneously calculate the digit sum.
- Return `x * digit_sum`.

This approach processes each digit only once, making it efficient.

---

## Algorithm

1. Convert the integer to a string.
2. Initialize:
   - `x = 0`
   - `digit_sum = 0`
3. Traverse every digit:
   - Skip `'0'`
   - Append the digit to `x`
   - Add the digit to `digit_sum`
4. Return `x * digit_sum`.

---

## Complexity Analysis

- **Time Complexity:** `O(d)`
- **Space Complexity:** `O(1)`

Where `d` is the number of digits in `n`.

---

## Key Concepts

- String traversal
- Digit manipulation
- Number construction
- Constant space optimization

---

## Solution

Implemented in **Python**.