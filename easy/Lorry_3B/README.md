# B. Lorry

## Problem
A lorry has a capacity of `v` cubic meters.

- Kayaks occupy **1 cubic meter**.
- Catamarans occupy **2 cubic meters**.

Each vehicle has a carrying capacity (value). Select a set of vehicles whose total volume does not exceed `v` while maximizing the total carrying capacity.

Output the maximum carrying capacity and the indices of the selected vehicles.

## Approach
Since there are only two possible sizes (1 and 2):

- Store kayaks and catamarans separately.
- Sort both groups in descending order of carrying capacity.
- Compute prefix sums for both groups.
- Try every possible number of catamarans.
- Fill the remaining capacity with the best available kayaks.
- Keep the combination with the maximum carrying capacity.

This guarantees the optimal solution efficiently.

## Algorithm
1. Separate kayaks and catamarans.
2. Sort each list by carrying capacity (descending).
3. Build prefix sums.
4. For every possible number of catamarans:
   - Calculate remaining volume.
   - Add the best possible kayaks.
   - Update the answer if the total carrying capacity improves.
5. Print the maximum carrying capacity and the selected indices.

## Complexity
- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)`

## Python Solution

```python
n, v = map(int, input().split())

kayaks = []
catamarans = []

for i in range(1, n + 1):
    t, p = map(int, input().split())
    if t == 1:
        kayaks.append((p, i))
    else:
        catamarans.append((p, i))

kayaks.sort(reverse=True)
catamarans.sort(reverse=True)

pre_kayaks = [0]
for p, _ in kayaks:
    pre_kayaks.append(pre_kayaks[-1] + p)

pre_catamarans = [0]
for p, _ in catamarans:
    pre_catamarans.append(pre_catamarans[-1] + p)

best = 0
best_cats = 0
best_kayaks = 0

max_cats = min(len(catamarans), v // 2)

for c in range(max_cats + 1):
    remaining = v - 2 * c
    k = min(len(kayaks), remaining)
    total = pre_catamarans[c] + pre_kayaks[k]

    if total > best:
        best = total
        best_cats = c
        best_kayaks = k

print(best)

answer = []
for i in range(best_cats):
    answer.append(str(catamarans[i][1]))
for i in range(best_kayaks):
    answer.append(str(kayaks[i][1]))

print(" ".join(answer))
```

## Key Concepts
- Greedy Strategy
- Sorting
- Prefix Sum
- Enumeration
- Optimization
```