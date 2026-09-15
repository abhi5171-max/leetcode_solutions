# A. Another Puzzle from Papyrus

## Problem Description

You are given two arrays `a` and `b` of length `n`.

You can perform two operations on array `a`:

1. Choose any index `i` and decrease `a[i]` by `1`.

   * Cost: `1` second.
2. Reorder all elements of `a` in any order.

   * Cost: `c` seconds.

The goal is to transform `a` into `b` with the minimum possible time.

If it is impossible, print `-1`.

---

## Approach

There are two possible strategies.

### 1. Do not reorder the array

We directly transform each `a[i]` into `b[i]`.

This is possible only when:

```text
a[i] >= b[i]
```

for every index.

The cost is:

```text
sum(a[i] - b[i])
```

---

### 2. Reorder the array once

If direct transformation is not optimal or not possible, we can reorder `a`.

To minimize the total number of decrements, sort both arrays and match corresponding elements:

```text
sorted(a) → sorted(b)
```

This gives the minimum possible subtraction cost.

The total cost becomes:

```text
c + sum(sorted(a[i]) - sorted(b[i]))
```

This is possible only if:

```text
sorted(a[i]) >= sorted(b[i])
```

for every `i`.

---

## Why Sorting Works

After reordering, we are free to choose which element of `a` corresponds to each element of `b`.

Matching smaller elements with smaller elements and larger elements with larger elements minimizes the total difference. Therefore, sorting both arrays gives the optimal matching.

We only need to consider **zero or one reorder operation**. Reordering more than once cannot provide any additional benefit because the array can already be arranged in the required optimal order after one operation.

---

## Algorithm

For each test case:

1. Check whether `a` can be transformed into `b` without reordering.
2. If possible, calculate its cost.
3. Sort both arrays.
4. Check whether the sorted `a` can be transformed into sorted `b`.
5. If possible, calculate the cost including `c`.
6. Take the minimum valid cost.
7. If neither strategy is possible, print `-1`.

---

## Complexity

For each test case:

* Sorting: `O(n log n)`
* Checking arrays: `O(n)`
* Space: `O(n)`

Overall:

```text
O(n log n)
```

per test case.

---

## Example

### Input

```text
3
3 5
5 2 3
2 3 4
3 3
1 2 3
4 5 6
4 4
4 5 2 3
3 5 1 2
```

### Output

```text
6
-1
3
```

### Explanation

For the first test case:

```text
a = [5, 2, 3]
b = [2, 3, 4]
```

Direct transformation is impossible because `2 < 3`.

After sorting:

```text
a = [2, 3, 5]
b = [2, 3, 4]
```

Only one decrement is needed:

```text
5 → 4
```

Including the reorder cost:

```text
5 + 1 = 6
```

Therefore, the answer is `6`.
