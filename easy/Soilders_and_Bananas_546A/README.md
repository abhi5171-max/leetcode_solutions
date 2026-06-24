# Soldier and Bananas - Codeforces

## Problem Statement

A soldier wants to buy `w` bananas. The first banana costs `k` dollars, the second costs `2k` dollars, the third costs `3k` dollars, and so on. Given the amount of money `n` that the soldier initially has, determine how much money he needs to borrow to buy all `w` bananas.

## Approach

The total cost of buying `w` bananas forms an arithmetic series:

Total Cost = `k × (1 + 2 + ... + w)`

Using the sum of the first `w` natural numbers:

`1 + 2 + ... + w = w × (w + 1) / 2`

Therefore,

```python
cost = k * w * (w + 1) // 2
```

The amount to borrow is:

```python
max(0, cost - n)
```

If the soldier already has enough money, the answer is `0`.

## Python Solution

```python
k, n, w = map(int, input().split())

cost = k * w * (w + 1) // 2
print(max(0, cost - n))
```

## Example

### Input

```
3 17 4
```

### Output

```
13
```

### Explanation

* Banana 1 → 3 dollars
* Banana 2 → 6 dollars
* Banana 3 → 9 dollars
* Banana 4 → 12 dollars

Total cost = `3 + 6 + 9 + 12 = 30`

Initial money = `17`

Money to borrow = `30 - 17 = 13`

## Complexity Analysis

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

## Tags

`Math` `Arithmetic Progression` `Implementation` `Codeforces`
