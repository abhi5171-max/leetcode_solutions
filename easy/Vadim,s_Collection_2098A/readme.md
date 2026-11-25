# Codeforces - A. Vadim's Collection

## Problem

Vadim has a beautiful 10-digit phone number.

A phone number is beautiful if the digit at each position is at least the required minimum:

| Position | Minimum digit |
|---:|---:|
| 1 | 9 |
| 2 | 8 |
| 3 | 7 |
| 4 | 6 |
| 5 | 5 |
| 6 | 4 |
| 7 | 3 |
| 8 | 2 |
| 9 | 1 |
| 10 | 0 |

The task is to rearrange the digits to obtain the smallest possible beautiful phone number.

## Approach: Greedy + Sorting

The goal is to construct the smallest valid number from left to right.

1. Sort all digits in ascending order.
2. For each position, determine its minimum required digit (`9 - i`).
3. Select the smallest remaining digit that is greater than or equal to the required digit.
4. Remove the selected digit and append it to the answer.
5. Repeat until all 10 positions are filled.

This greedy strategy minimizes each position while ensuring that the remaining digits can satisfy the subsequent positions.

## Python Solution

```python
t = int(input())

for _ in range(t):
    s = input().strip()

    digits = sorted(s)
    ans = []

    for i in range(10):
        required = 9 - i

        for j in range(len(digits)):
            if int(digits[j]) >= required:
                ans.append(digits.pop(j))
                break

    print("".join(ans))
```

## Complexity Analysis

Let `n` be the number of digits.

- **Time Complexity:** `O(n²)` because we search for and remove a valid digit for each position.
- **Space Complexity:** `O(n)` for storing the sorted digits and answer.

Since `n = 10`, the solution easily satisfies the time limit.

## Key Concepts

- Greedy Algorithm
- Sorting
- String Manipulation
- Lexicographically Smallest Arrangement

## Key Takeaway

When constructing the smallest possible number under position-based constraints, make the smallest valid choice at each position. This is a useful greedy pattern for rearrangement problems.
