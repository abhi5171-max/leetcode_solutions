# A. Vasya and Socks

## Problem
Vasya starts with `n` pairs of socks.

- Every day he uses one pair.
- Every `m`-th day, his mother buys one new pair in the evening.
- Determine how many consecutive days Vasya can wear socks.

### Example
**Input**
```
2 2
```

**Output**
```
3
```

---

## Approach

Simulate the process day by day.

For each day:
1. Use one pair of socks.
2. Increase the day counter.
3. If the current day is divisible by `m`, add one new pair.

Continue until no socks remain.

Since `n ≤ 100`, simulation is fast and sufficient.

---

## Algorithm
1. Read `n` and `m`.
2. While socks are available:
   - Increment the day count.
   - Decrease socks by one.
   - If the current day is a multiple of `m`, add one sock pair.
3. Print the total number of days.

---

## Complexity Analysis

- **Time Complexity:** `O(answer)`
- **Space Complexity:** `O(1)`

---

## Concepts Used

- Simulation
- Loops
- Conditional Statements