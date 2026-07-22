# C. Hexadecimal's Numbers

## Problem
Given an integer `n`, count how many numbers from `1` to `n` consist only of the decimal digits **0** and **1**.

### Example
**Input**
```
10
```

**Output**
```
2
```

Numbers are:
- 1
- 10

---

## Approach

Since `n ≤ 10^9`, every valid number has at most 10 digits.

Generate every possible number consisting only of digits `0` and `1` using **DFS (Depth-First Search)**.

For each generated number:
- Stop if it becomes greater than `n`.
- Otherwise count it.
- Continue by appending:
  - `0`
  - `1`

The total number of generated numbers is very small (1023), making this solution extremely efficient.

---

## Algorithm
1. Start DFS from `1`.
2. If the current number is greater than `n`, return.
3. Count the current number.
4. Recurse for:
   - `number × 10`
   - `number × 10 + 1`
5. Print the total count.

---

## Complexity Analysis

- **Time Complexity:** `O(1023)` (constant)
- **Space Complexity:** `O(10)` (recursion depth)

---

## Concepts Used

- DFS
- Recursion
- Backtracking
- Number Generation