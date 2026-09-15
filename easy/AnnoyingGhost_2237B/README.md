# B. Annoying the Ghost

## Problem Description

We have an array `a` of `n` pile sizes and a strictly increasing target array `b`.

The process has two stages:

1. We can **only increase** every element of `a`.
2. We can swap adjacent elements any number of times.

We need to make the final array exactly equal to `b`.

The goal is to minimize the number of adjacent swaps.

---

## Key Observation

After the first stage, every original element `a[i]` must become some target value `b[j]`.

Since we can only increase:

```text
a[i] <= b[j]
```

must hold for the target value assigned to it.

Therefore, an element `a[i]` can be assigned to any `b[j] >= a[i]`.

Because `b` is strictly increasing, we can process the target values from smallest to largest.

For each `b[j]`, we should choose the **rightmost unused element** in `a` that can be increased to `b[j]`.

Why the rightmost one?

Choosing a later position leaves earlier elements available for later target values and minimizes the total number of adjacent swaps.

---

## Counting Swaps

Suppose the element originally at position `p` is assigned to target position `j`.

When elements are moved using adjacent swaps, the number of swaps can be calculated by tracking how many already-selected elements are before it.

A simpler implementation uses a Fenwick Tree (BIT).

Initially, every position is available.

For each target `b[j]`:

* Find the rightmost available position `p` with `a[p] <= b[j]`.
* If no such position exists, the transformation is impossible.
* The number of currently available elements before `p` determines how far this element has to move.
* Remove position `p` from the Fenwick Tree.

---

## Alternative View

We need to find a permutation of the original elements that can be transformed into:

```text
b1 < b2 < ... < bn
```

using only increments.

The optimal matching is obtained greedily:

```text
For every target b[j]:
    choose the rightmost unused a[i] such that a[i] <= b[j]
```

This greedy choice minimizes inversions, which are exactly the number of adjacent swaps required.

---

## Algorithm

For every test case:

1. Create a list of `(a[i], i)`.
2. Sort elements by value.
3. Process `b` in increasing order.
4. Among elements with `a[i] <= b[j]`, select the rightmost unused position.
5. If no element is available, print `-1`.
6. Count how many remaining elements are before the selected position.
7. Remove that position from the available positions.
8. The accumulated count is the answer.

A Fenwick Tree allows each insertion/removal/query in `O(log n)`.

---

## Complexity

For each test case:

* Sorting: `O(n log n)`
* Processing elements: `O(n log n)`
* Memory: `O(n)`

Since the sum of `n` over all test cases is at most `2000`, this easily fits within the limits.

---

## Example

For:

```text
a = [2, 2, 1]
b = [1, 2, 3]
```

The `1` must be assigned to the first target position.

It originally occurs at position `3`, so it must move two positions to the left:

```text
[2, 2, 1]
   ↓
[2, 1, 2]
   ↓
[1, 2, 2]
```

Therefore the answer is:

```text
2
```

---

## Important

The first stage costs nothing for the purpose of this problem. We only need to minimize the number of swaps in the second stage.

If any `a[i]` is greater than every possible target value it could be assigned to, the answer is `-1`.
