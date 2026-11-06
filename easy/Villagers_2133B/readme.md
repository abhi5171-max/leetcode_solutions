# B. Villagers

**Platform:** Codeforces  
**Problem:** B. Villagers  
**Language:** Python 3  
**Topics:** Greedy, Sorting, Prefix Sum, Suffix Sum

## Problem Summary

There are `n` villagers, each having an initial grumpiness value.

An operation consists of:
- Selecting two villagers.
- Paying `max(gi, gj)` emeralds.
- Decreasing both grumpiness values by `min(gi, gj)`.
- Making the two villagers friends.

The objective is to make the friendship graph connected while minimizing the total emeralds spent.

## Approach: Greedy + Sorting

### 1. Sorting

First, sort the grumpiness values in ascending order.

Pairing smaller values together helps minimize the total cost.

An operation between two villagers with grumpiness `x` and `y` costs `max(x, y)` and makes at least one of their grumpiness values zero.

This allows us to connect the resulting zero-grumpiness villagers without spending additional emeralds.

### 2. When n is even

Pair adjacent elements in the sorted array.

The minimum cost is:

`a[1] + a[3] + a[5] + ...`

Python implementation:

```python
ans = sum(a[1::2])
```

### 3. When n is odd

One villager must remain unpaired.

We try every possible valid position for this unpaired villager.

- `pref[i]` stores the minimum pairing cost for the first `i` elements.
- `suff[i]` stores the minimum pairing cost for the elements from index `i` to the end.
- We combine both costs while leaving one element unpaired.

The answer is:

`min(pref[i] + suff[i+1])`

for every even index `i`.

## Complexity Analysis

| Operation | Complexity |
|---|---|
| Sorting | O(n log n) |
| Prefix calculation | O(n) |
| Suffix calculation | O(n) |
| Finding minimum | O(n) |

**Overall Time Complexity:** O(n log n) per test case.

**Space Complexity:** O(n) for prefix and suffix arrays.

## Key Learning

- Sorting helps identify optimal adjacent pairings.
- Greedy strategies can simplify graph connectivity problems.
- Prefix and suffix arrays help efficiently evaluate different choices.
- Always consider separate cases for even and odd array lengths.

