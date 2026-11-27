# Codeforces - A. Ideal Generator

## Problem

Given an integer `k`, determine whether it is an ideal generator.

A number `k` is an ideal generator if every integer `n >= k` can be represented as the sum of a palindromic array containing exactly `k` positive integers.

A palindromic array reads the same from left to right and right to left.

## Approach: Mathematical Observation

There are two cases based on the parity of `k`.

### Case 1: Odd k

When `k` is odd, there is one middle element that does not require a matching element.

For any `n >= k`, we can construct a palindrome consisting of:

- `1` in every position except the middle.
- `n - k + 1` in the middle position.

For example, if `k = 3` and `n = 10`:

```text
[1, 8, 1]
```

The array is palindromic, contains exactly three positive integers, and its sum is 10.

Therefore, every odd `k` is an ideal generator.

### Case 2: Even k

When `k` is even, every element in a palindromic array has a matching element.

Therefore, its sum must always be even.

However, not every integer greater than or equal to `k` is even.

For example, `k + 1` is odd, so it cannot be represented.

Therefore, every even `k` is not an ideal generator.

### Final Condition

```text
If k is odd:
    YES
Otherwise:
    NO
```

## Python Solution

```python
t = int(input())

for _ in range(t):
    k = int(input())

    if k % 2 == 1:
        print("YES")
    else:
        print("NO")
```

## Complexity Analysis

- **Time Complexity:** `O(1)` per test case.
- **Space Complexity:** `O(1)` auxiliary space.

## Key Concepts

- Mathematical Observation
- Palindromic Arrays
- Odd and Even Numbers
- Parity

## Key Takeaway

Recognizing whether the length of a palindrome is odd or even makes this problem straightforward. Odd-length palindromes have a flexible middle element, while even-length palindromes always have an even sum.
