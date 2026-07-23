# 🍂 A. Indian Summer

## Problem Overview

Alyona is collecting fallen leaves in a forest. She only keeps a leaf if its **tree species** and **color** combination has not already been collected.

The task is to determine how many **unique (species, color)** pairs exist among the given leaves.

## Approach

* Read the number of leaves.
* Store each `(species, color)` pair in a Python `set`.
* Since sets automatically remove duplicates, the final answer is simply the size of the set.

## Algorithm

1. Read `n`.
2. Initialize an empty set.
3. For each leaf:

   * Read its species and color.
   * Insert the pair into the set.
4. Print the number of unique pairs.

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

## Key Concepts

* Sets
* Tuples
* Duplicate removal
* Basic data structures

## Python Solution

```python
n = int(input())

unique_leaves = set()

for _ in range(n):
    species, color = input().split()
    unique_leaves.add((species, color))

print(len(unique_leaves))
```
