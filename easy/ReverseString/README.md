📄 README – Reverse Integer
# Reverse Integer

## Problem Statement

Given a signed 32-bit integer `x`, return its digits reversed.

If reversing the integer causes it to go outside the signed 32-bit integer range:

[-2³¹, 2³¹ − 1]

return `0`.

The solution must not rely on 64-bit integer storage.

---

## Examples

### Example 1

Input:

x = 123


Output:

321


### Example 2

Input:

x = -123


Output:

-321


### Example 3

Input:

x = 120


Output:

21


---

## Approach

- Store the sign of the number.
- Work with the absolute value.
- Extract digits one by one using modulo (`%`).
- Build the reversed integer using multiplication and addition.
- Before appending a digit, check whether the new value would overflow the 32-bit signed integer range.
- Restore the original sign.

---

## Algorithm

1. Save the sign of the number.
2. Convert the number to its absolute value.
3. Initialize `reverse = 0`.
4. Repeat until the number becomes zero:
   - Extract the last digit.
   - Remove the last digit.
   - Check for overflow.
   - Append the digit to the reversed number.
5. Return the reversed number with its original sign.

---

## Complexity Analysis

- **Time Complexity:** `O(log₁₀ n)`
- **Space Complexity:** `O(1)`

---

## Key Concepts

- Integer manipulation
- Modulo arithmetic
- Overflow detection
- Mathematical algorithms
- Edge case handling

---

## Solution

Implemented in **Python**.