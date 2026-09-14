# A. Another Popcount Problem

## Problem Statement

Given two integers `n` and `k`, construct a sequence of `k` non-negative integers such that:

* The sum of all elements is at most `n`.
* The total number of set bits among all elements is maximized.

We only need to output the maximum possible total number of set bits.

---

## Approach

To obtain `p` set bits in a number with the minimum possible value, we use:

```text
2^p - 1
```

For example:

* `1` → `1` set bit → value `1`
* `3` → `2` set bits → value `3`
* `7` → `3` set bits → value `7`
* `15` → `4` set bits → value `15`

Adding set bits to a number has incremental costs:

```text
1, 2, 4, 8, ...
```

Since there are `k` numbers, each incremental cost can be used at most `k` times.

We greedily choose the cheapest available set bits until the total cost exceeds `n`.

---

## Algorithm

For each test case:

1. Give as many of the `k` numbers as possible their first set bit.
2. The first set bit costs `1`.
3. Additional set bits cost `1, 2, 4, 8, ...`.
4. For each cost, add as many set bits as possible, up to `k`.
5. Continue until the remaining sum is insufficient.

---

## Complexity

For each test case:

* **Time Complexity:** `O(log n)`
* **Space Complexity:** `O(1)`

---

## Example

### Input

```text
6
2 1
3 1
6 2
14142 137205
1000000 100
1000000 1000000
```

### Output

```text
1
2
4
14142
1322
1000000
```
