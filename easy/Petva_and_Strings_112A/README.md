# 112A - Petya and Strings

## Problem
Given two strings of equal length, compare them lexicographically without considering letter case.

## Approach
- Convert both strings to lowercase.
- Compare them directly using Python's string comparison operators.
- Print:
  - `-1` if the first string is smaller.
  - `1` if the first string is larger.
  - `0` if both strings are equal.

## Complexity
- Time: O(n)
- Space: O(1)