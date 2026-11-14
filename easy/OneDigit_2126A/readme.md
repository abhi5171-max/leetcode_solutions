# Common Digit

## Problem Statement

You are given an integer `n`.

Find the smallest non-negative integer `y` such that `n` and `y` share at least one common decimal digit.

In other words, at least one digit must appear in both numbers.

## Approach: Greedy + Digit Extraction

The key observation is that the smallest valid answer is simply the **smallest digit present in `n`**.

Why?

- We can choose `y` as a single-digit number.
- If we choose the smallest digit present in `n`, both numbers share that digit.
- No smaller non-negative integer can satisfy the condition.

Therefore:

`Answer = Minimum digit in n`

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    n = input().strip()
    print(min(int(digit) for digit in n))
```

## Example

**Input:**
```text
5
6
96
78
122
696
```

**Output:**
```text
6
6
7
1
6
```

## Dry Run

For `n = 696`:

- Digits: `6, 9, 6`
- Minimum digit: `6`
- Answer: `6`

For `n = 122`:

- Digits: `1, 2, 2`
- Minimum digit: `1`
- Answer: `1`

## Complexity Analysis

- **Time Complexity:** `O(d)` per test case, where `d` is the number of digits in `n`.
- **Space Complexity:** `O(1)` auxiliary space.

## Key Learnings

- Extracting digits from a number using strings.
- Applying greedy observations to find an optimal answer.
- Simplifying a search problem into a minimum-digit calculation.

---

**Final Observation:** The smallest digit in the given number is always the answer.