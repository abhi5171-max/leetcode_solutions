# A. Redstone?

**Platform:** Codeforces  
**Problem:** A. Redstone?  
**Language:** Python 3  
**Topics:** Mathematics, Greedy, Arrays, Sets

## Problem Summary

Steve has `n` gears, each containing a certain number of teeth.

He arranges the gears in a row and spins the first gear at 1 revolution per second.

The speed of every subsequent gear depends on the ratio between its teeth and the teeth of the previous gear.

The task is to determine whether the gears can be rearranged so that the last gear also spins at exactly 1 revolution per second.

## Approach: Mathematical Observation + Set

The speed of the second gear is:

`a1 / a2`

The speed of the third gear is:

`(a2 / a3) * (a1 / a2)`

After simplifying, the intermediate values cancel.

Therefore, the final speed becomes:

`a1 / an`

For the final speed to equal 1:

`a1 = an`

Since Steve can rearrange the gears freely, we only need to check whether at least two gears have the same number of teeth.

### Algorithm

1. Read the number of gears.
2. Store all gear values in an array.
3. Convert the array into a set.
4. If the set size is smaller than the array size, duplicates exist.
5. Print `YES` if duplicates exist; otherwise print `NO`.

## Python Code

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) < n:
        print("YES")
    else:
        print("NO")
```

## Complexity Analysis

- **Time Complexity:** O(n) average per test case for set construction.
- **Space Complexity:** O(n) for storing distinct elements.

## Key Learnings

- Mathematical simplification can eliminate unnecessary simulation.
- A set helps identify duplicate elements efficiently.
- Gear speed ratios can be simplified using cancellation.
- Understanding the final condition is often more important than simulating every operation.