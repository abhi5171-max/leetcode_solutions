# Codeforces — A. Yes or Yes

## Problem Description

Given a string `s` consisting only of `Y` and `N`, we can repeatedly combine two adjacent characters using logical OR. Combining two `Y` characters is forbidden.

Determine whether the string can be reduced to a single character without ever combining two `Y` characters.

## Approach

The key observation is that the operation is impossible whenever two adjacent characters are both `Y`.

- If the string contains `"YY"`, the answer is `NO`.
- Otherwise, the answer is `YES`, because we can combine adjacent characters without combining two `Y` characters.

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case, where `n` is the length of the string.
- **Space Complexity:** `O(n)` for storing the input string.

## Key Concepts

- String manipulation
- Substring checking
- Greedy observation
