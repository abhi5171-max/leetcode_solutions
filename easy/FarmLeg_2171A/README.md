# A. Shizuku Hoshikawa and Farm Legs

**Platform:** Codeforces  
**Language:** Python 3  
**Topics:** Math, Implementation

## Problem Description

A farm contains only chickens and cows. Each chicken has 2 legs, and each cow has 4 legs. Given the total number of legs, calculate the number of possible configurations.

Zero chickens or zero cows are allowed.

## Approach

1. Read the total number of legs `n`.
2. If `n` is odd, print `0` because both animals have an even number of legs.
3. Otherwise, print `n // 4 + 1`, representing the possible numbers of cows from zero to `n // 4`.

## Example

**Input

```text
5
2
3
4
6
100
```

**Output

```text
1
0
2
2
26
```

## Complexity Analysis

- **Time Complexity:** `O(1)` per test case.
- **Space Complexity:** `O(1)`.

## Key Learning

Use parity to determine whether a solution is possible, then count the possible numbers of cows.
