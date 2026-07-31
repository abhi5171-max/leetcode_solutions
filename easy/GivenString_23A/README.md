# 🔤 You're Given a String...

## Problem Overview

Given a lowercase string, determine the length of the longest substring that appears at least twice in the string. The repeated occurrences are allowed to overlap.

## Approach

* Try every possible substring length from `1` to `n-1`.
* For each length:

  * Generate all substrings of that length.
  * Store each substring in a set.
  * If a substring is encountered again, update the maximum answer.

Since the maximum string length is only **100**, this brute-force approach is efficient enough.

## Algorithm

1. Read the input string.
2. For every possible substring length:

   * Generate all substrings.
   * Track previously seen substrings using a set.
   * If a substring repeats, update the answer.
3. Print the maximum repeated substring length.

## Complexity Analysis

* **Time Complexity:** `O(n³)`
* **Space Complexity:** `O(n²)`

## Concepts Used

* Strings
* Brute Force
* Hash Set
* Sliding Window Traversal

## Tags

`Codeforces` `Strings` `Brute Force` `Hashing` `Python`
