# A. Business Trip

## Problem
Petya needs his flower to grow by at least **k centimeters** during the year. For each of the 12 months, the flower grows by a known amount if he waters it.

Determine the **minimum number of months** Petya should water the flower so that the total growth is at least `k`. If it is impossible, output `-1`.

## Approach
- If `k == 0`, no watering is required, so the answer is `0`.
- Sort the monthly growth values in descending order.
- Greedily choose the months with the highest growth.
- Keep adding growth until the accumulated growth reaches or exceeds `k`.
- If all 12 months are used and the total growth is still less than `k`, output `-1`.

## Algorithm
1. Read `k` and the 12 monthly growth values.
2. Handle the special case `k == 0`.
3. Sort the growth values in descending order.
4. Iterate through the sorted list:
   - Add the current month's growth.
   - Count the selected months.
   - Stop once total growth ≥ `k`.
5. If the target is never reached, print `-1`.

## Complexity
- **Time Complexity:** `O(12 log 12)` (constant time in practice)
- **Space Complexity:** `O(1)`

## Python Solution

```python
k = int(input())
growth = list(map(int, input().split()))

if k == 0:
    print(0)
    exit()

growth.sort(reverse=True)

total = 0
months = 0

for g in growth:
    total += g
    months += 1
    if total >= k:
        print(months)
        exit()

print(-1)
```

## Key Concepts
- Greedy Algorithm
- Sorting
- Simulation