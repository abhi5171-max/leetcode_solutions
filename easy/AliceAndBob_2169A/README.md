# A. Alice and Bob

**Platform:** Codeforces  
**Language:** Python 3  
**Topic:** Greedy Algorithm

## Problem Description

Alice chooses an integer `a`, and Bob must choose an integer `b`. Each marble awards a point to the player whose chosen integer is closer to its value. If both distances are equal, Alice wins.

Bob must choose `b` to maximize his points.

## Approach

Count the marble values that are:

- Less than `a`
- Greater than `a`
- Equal to `a`

Marbles equal to `a` cannot be won by Bob.

If the number of marbles greater than `a` is at least the number less than `a`, choose `b = a + 1`. Otherwise, choose `b = a - 1`.

This strategy maximizes Bob's score.

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case.
- **Space Complexity:** `O(n)` to store the marble values.

## Example

**Input

```text
3
7 21
10 20 30 40 50 60 70
6 500
200 200 300 500 600 600
2 7
7 7
```

**Output

```text
22
499
6
```

*Note: Multiple choices of `b` may be optimal, so the output can differ from the problem statement's sample output.*
