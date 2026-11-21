# Codeforces - A. Energy Crystals (2111A)

## Problem Statement

There are three energy crystals, initially having energy levels `[0, 0, 0]`.

Each crystal must reach exactly `x`.

In one operation, we can increase the energy level of any one crystal by a positive amount. However, after every operation, the following condition must hold for every pair of crystals:

\[
a_i \geq \left\lfloor \frac{a_j}{2} \right\rfloor
\]

The task is to find the minimum number of operations required to charge all three crystals to level `x`.

## Approach: Greedy + Simulation

The key observation is that we should always increase the crystal with the smallest energy level.

First, sort the three crystal energy levels:

\[
a_1 \leq a_2 \leq a_3
\]

To maintain the synchronization condition, the smallest crystal can be increased up to:

\[
a_1 = \min(x, 2a_2+1)
\]

After updating the smallest crystal:

1. Sort the three energy levels again.
2. Increase the operation counter.
3. Repeat until the smallest crystal reaches `x`.

When the smallest crystal reaches `x`, all three crystals have reached the target.

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    x = int(input())

    a = [0, 0, 0]
    ans = 0

    while a[0] < x:
        a[0] = min(x, 2 * a[1] + 1)

        a.sort()

        ans += 1

    print(ans)
```

## Example

**Input:**

```text
7
1
5
14
2025
31415
536870910
1000000000
```

**Output:**

```text
3
7
9
23
31
59
61
```

## Complexity Analysis

- **Time Complexity:** O(log x) per test case because the energy levels grow approximately exponentially.
- **Space Complexity:** O(1) because only three crystal values and a counter are maintained.

## Key Learnings

- Greedy algorithms and optimal local choices.
- Sorting a small collection to identify the minimum element.
- Understanding mathematical constraints before performing an operation.
- Using simulation to construct an optimal sequence of operations.

---

**Problem:** A. Energy Crystals  
**Problem Code:** 2111A  
**Platform:** Codeforces  
**Language:** Python 3