# Army

## Problem
The Berland army consists of `n` ranks. Moving from rank `i` to rank `i+1` requires `d[i]` years.

Given Vasya's current rank `a` and desired rank `b`, determine how many more years he must serve to reach rank `b`.

## Approach
The years required are simply the sum of all promotion times between ranks `a` and `b`.

For ranks:
- `a → a+1`
- `a+1 → a+2`
- ...
- `b-1 → b`

Sum the corresponding values in the array.

## Algorithm
1. Read `n`.
2. Read the promotion years array.
3. Read the current and target ranks.
4. Sum the values from index `a-1` to `b-2`.
5. Print the result.

## Complexity Analysis
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (excluding input storage)

## Concepts Used
- Arrays
- Prefix interval summation
- Basic indexing