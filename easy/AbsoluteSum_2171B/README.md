# Codeforces — B. Yuu Koito and Minimum Absolute Sum

## Problem

Given an array of nonnegative integers containing `-1` as blank elements, replace all blanks with nonnegative integers to minimize the absolute sum of the difference array. If multiple arrays achieve the minimum, choose the lexicographically smallest one.

## Approach

The difference array is defined as:

\[
b_i = a_{i+1} - a_i
\]

Its sum telescopes:

\[
\sum_{i=1}^{n-1} b_i = a_n-a_1
\]

Thus, the objective is to minimize `abs(a[n-1] - a[0])`.

1. If both endpoints are `-1`, replace both with `0`.
2. If only the first endpoint is `-1`, set it equal to the last endpoint.
3. If only the last endpoint is `-1`, set it equal to the first endpoint.
4. Replace all remaining `-1` elements with `0`.
5. Print the minimum absolute difference and the resulting array.

Choosing zero for unknown middle elements ensures the lexicographically smallest array because these elements do not affect the objective.

## Complexity Analysis

- **Time Complexity:** \(O(n)\) per test case.
- **Space Complexity:** \(O(n)\) to store the array.

## Language

Python 3

## Key Learning

The main insight is that a sum of consecutive differences telescopes to the difference between the last and first elements. Recognizing this reduces the problem to choosing the endpoints optimally.
