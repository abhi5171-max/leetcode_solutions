# B. Martian Dollar

## Problem Overview
Vasya has `b` bourles and knows the Martian dollar exchange rate for the next `n` days.

He may:
- Buy an integer number of dollars on exactly one day.
- Sell all of them on a later day.
- Make at most one transaction.

The goal is to maximize the amount of bourles he has after the final day.

## Approach
- Try every possible buying day.
- Buy the maximum number of whole dollars.
- Keep the remaining bourles.
- Try every later selling day.
- Calculate the total money after selling.
- Track the maximum value obtained.

Also consider the possibility of making no transaction.

## Algorithm
1. Initialize the answer as the initial bourles.
2. For every buying day:
   - Compute:
     - Number of dollars purchased.
     - Remaining bourles.
3. For every later selling day:
   - Calculate:
     ```
     total = remaining + dollars × selling_price
     ```
   - Update the maximum answer.
4. Print the maximum amount.

## Correctness
The algorithm checks every valid pair of buying and selling days while always purchasing the maximum possible number of dollars. Since all possible transactions are evaluated, the maximum obtainable bourles is guaranteed to be found.

## Complexity Analysis
- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(1)` (excluding input storage)

## Python Solution

```python
n, b = map(int, input().split())
prices = list(map(int, input().split()))

ans = b

for i in range(n):
    dollars = b // prices[i]
    remaining = b % prices[i]

    for j in range(i + 1, n):
        money = remaining + dollars * prices[j]
        ans = max(ans, money)

print(ans)
```

## Key Concepts
- Brute Force
- Simulation
- Greedy Purchase
- Nested Iteration
```