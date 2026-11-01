# A. Candies for Nephews

**Platform:** Codeforces  
**Problem:** A. Candies for Nephews

## Problem Description

Monocarp has three nephews and initially owns `n` candies.

He wants to distribute all candies equally among the three nephews.

Find the minimum number of additional candies he needs to buy so that the total number of candies is divisible by 3.

## Approach: Modulo Operator

The total number of candies must be divisible by 3.

We calculate the remainder using:

`n % 3`

The minimum additional candies required are:

`(3 - n % 3) % 3`

This formula gives:

- `0` if the number is already divisible by 3.
- `1` if the remainder is 2.
- `2` if the remainder is 1.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    print((3 - n % 3) % 3)
```

## Example

**Input:**

```text
2
7
24
```

**Output:

```text
2
0
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case.
- **Space Complexity:** O(1).

## Key Concepts

- Modulo Operator
- Arithmetic Operations
- Divisibility
- Basic Implementation

## Key Takeaway

A number must be divisible by 3 to distribute candies equally among three nephews. The modulo operator helps calculate the minimum additional candies required.

**Problem Status:** Solved
