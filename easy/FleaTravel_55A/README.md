# Codeforces A. Flea Travel

## Problem Statement

A flea is sitting on one of `n` hassocks arranged in a circle.

After minute `k`, the flea jumps clockwise over `k - 1` hassocks, meaning it moves forward by `k` positions.

For example:

* After the 1st minute → moves `1` position.
* After the 2nd minute → moves `2` positions.
* After the 3rd minute → moves `3` positions.
* And so on.

The flea has infinitely much time to jump.

The task is to determine whether the flea will eventually visit **all `n` hassocks**.

---

## Approach

The total distance traveled after `k` minutes is:

[
1 + 2 + 3 + \dots + k
]

which is the `k`-th triangular number:

[
T_k = \frac{k(k+1)}{2}
]

Considering the positions modulo `n`, the flea visits all hassocks exactly when `n` is a **power of 2**.

Therefore, we only need to check whether `n` is a power of 2.

A positive integer is a power of 2 if:

```python
n & (n - 1) == 0
```

---

## Python 3 Solution

```python
n = int(input())

if n & (n - 1) == 0:
    print("YES")
else:
    print("NO")
```

---

## Example 1

### Input

```text
1
```

### Output

```text
YES
```

`1` is a power of 2, so all hassocks can be visited.

---

## Example 2

### Input

```text
3
```

### Output

```text
NO
```

`3` is not a power of 2, so not all hassocks will be visited.

---

## Why Does `n & (n - 1)` Work?

Powers of 2 have exactly one `1` in their binary representation.

For example:

```text
8  = 1000
7  = 0111
-----------
&  = 0000
```

Therefore:

```text
n & (n - 1) == 0
```

is true only for powers of 2.

Examples:

```text
1  → YES
2  → YES
4  → YES
8  → YES
16 → YES

3  → NO
5  → NO
6  → NO
10 → NO
```

---

## Complexity Analysis

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`


