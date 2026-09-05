
# Codeforces — A. Dividing Orange

## Problem

Ms Swan has an orange consisting of `n × k` segments and `k` children.

Each child has requested one specific segment. We need to divide all the orange segments so that:

* Every child gets exactly `n` segments.
* Each child receives their requested segment.
* No segment is given to more than one child.

The order of segments assigned to a child does not matter.

---

## Approach

The main idea is to process the requested segments in **descending order**.

For each child:

1. Give the child their requested segment.
2. Fill the remaining `n - 1` positions with the largest unused segments that are smaller than the requested segment.
3. Mark every assigned segment as used.

Since all requested segment numbers are distinct and the problem guarantees that a solution exists, this process produces a valid division.

### Why process in descending order?

Consider a child requesting segment `x`.

When we process larger requested segments first, those children take the necessary smaller segments before we reach the current child. Therefore, when processing the current request, we can safely choose unused segments smaller than it without taking another child's requested segment.

---

## Example

### Input

```text
2 2
4 1
```

The children want segments `4` and `1`.

Process `4` first:

```text
Child 1 → 4, 3
```

Then process `1`:

```text
Child 2 → 1, 2
```

### Output

```text
4 3
1 2
```

This is valid because:

* Child 1 gets exactly 2 segments and gets segment `4`.
* Child 2 gets exactly 2 segments and gets segment `1`.
* Every segment from `1` to `4` is used exactly once.

---

## Algorithm

1. Read `n`, `k`, and the requested segments.
2. Store each requested segment together with its child index.
3. Sort the requests in descending order.
4. Create a `used` array to track assigned segments.
5. For every child:

   * Assign their requested segment.
   * Move downward from `requested - 1`.
   * Assign unused segments until the child has `n` segments.
6. Print the segments assigned to each child.

---

## Complexity

There are `n × k` total segments.

* **Time Complexity:** `O(n × k + k log k)`
* **Space Complexity:** `O(n × k)`

Since `n, k ≤ 30`, this easily fits within the limits.

---

## Key Takeaway

The important trick is:

> **Process requested segments from largest to smallest and fill each child's remaining slots with unused smaller segments.**

This guarantees that every child gets their requested segment while all segments are distributed exactly once.

\
