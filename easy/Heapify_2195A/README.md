# B. Heapify 1

## Problem

You are given a permutation `a` of length `n`.

You can perform the following operation any number of times:

- Choose an index `i` such that `1 ≤ i ≤ n/2`.
- Swap `a[i]` and `a[2i]`.

The goal is to determine whether the permutation can be sorted in increasing order.

---

## Key Observation

We can only swap an index with its double:

```text
i ↔ 2i
```

Therefore, indices are divided into independent groups:

```text
1 → 2 → 4 → 8 → ...
3 → 6 → 12 → ...
5 → 10 → 20 → ...
7 → 14 → 28 → ...
```

An element can move only within the group containing its index.

Every positive integer can be uniquely written as:

```text
x = odd_part × 2^k
```

So two numbers belong to the same group if and only if their **odd parts are equal**.

For the permutation to be sortable, for every position `i`:

```text
odd_part(i) == odd_part(a[i])
```

If this condition holds for every position, the answer is `YES`; otherwise, it is `NO`.

---

## Example

### Input

```text
2
5
1 4 3 2 5
5
1 4 2 3 5
```

### First Test Case

```text
a = [1, 4, 3, 2, 5]
```

The elements `2` and `4` can be swapped because:

```text
2 ↔ 4
```

After swapping:

```text
[1, 2, 3, 4, 5]
```

Therefore:

```text
YES
```

### Second Test Case

```text
a = [1, 4, 2, 3, 5]
```

At index `3`, the value is `2`.

```text
odd_part(3) = 3
odd_part(2) = 1
```

They belong to different groups, so `2` can never reach position `3`.

Therefore:

```text
NO
```

---

## Python Solution

```python
def odd_part(x):
    while x % 2 == 0:
        x //= 2
    return x


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    possible = True

    for i in range(n):
        # Convert 0-based index to 1-based index
        index = i + 1

        if odd_part(index) != odd_part(a[i]):
            possible = False
            break

    print("YES" if possible else "NO")
```

---

## How the Code Works

### 1. Find the odd part

```python
def odd_part(x):
    while x % 2 == 0:
        x //= 2
    return x
```

For example:

```text
odd_part(12)
12 → 6 → 3
```

So:

```text
odd_part(12) = 3
```

Similarly:

```text
odd_part(24) = 3
```

Therefore `12` and `24` belong to the same group.

---

### 2. Check Every Position

```python
for i in range(n):
    index = i + 1

    if odd_part(index) != odd_part(a[i]):
        possible = False
        break
```

If the index and its current value have different odd parts, that value cannot be moved to its correct position.

---

## Complexity

For each element, we repeatedly divide by `2`.

The number of divisions is at most `O(log n)`.

Therefore:

- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(n)` for storing the permutation.

---

## Important Concept

The operation:

```text
i ↔ 2i
```

does **not** allow arbitrary swaps.

It creates independent connected components based on the odd part of the index.

### Groups

```text
1:  1, 2, 4, 8, 16, ...
