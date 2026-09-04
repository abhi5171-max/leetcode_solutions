Here’s the clean **Python 3 solution** and a **README-style explanation** for Codeforces **B. Effective Approach**.

## Python 3 Solution

```python
n = int(input())
a = list(map(int, input().split()))

# pos[x] = position of value x in the permutation
pos = [0] * (n + 1)

for i in range(n):
    pos[a[i]] = i + 1

m = int(input())
queries = list(map(int, input().split()))

vasya = 0
petya = 0

for x in queries:
    p = pos[x]

    # Search from left
    vasya += p

    # Search from right
    petya += n - p + 1

print(vasya, petya)
```

# README — B. Effective Approach

## Problem

We are given a permutation of numbers from `1` to `n`.

For every query, we need to find a particular number using two different linear-search approaches:

* **Vasya:** searches from left to right.
* **Petya:** searches from right to left.

We need the **total number of comparisons** made by both approaches for all queries.

---

## Key Observation

Because the array is a **permutation**, every number occurs exactly once.

Suppose a number `x` is located at position:

```text
p
```

using 1-based indexing.

### Vasya's comparisons

Vasya starts from index `1`:

```text
1, 2, 3, ..., p
```

Therefore:

```text
Vasya comparisons = p
```

### Petya's comparisons

Petya starts from index `n` and moves backwards:

```text
n, n-1, ..., p
```

Therefore:

```text
Petya comparisons = n - p + 1
```

So if we know the position of every value, each query can be answered in **O(1)**.

---

## Why not perform linear search directly?

If we search the array separately for every query, the complexity can become:

```text
O(n × m)
```

Since:

```text
n ≤ 100000
m ≤ 100000
```

the worst case would be:

```text
10^5 × 10^5 = 10^10
```

operations, which is too slow.

Instead, preprocess the positions of all values.

---

## Algorithm

For the array:

```text
a1 a2 a3 ... an
```

create:

```python
pos[value] = index
```

For example:

```text
Array:
3 1 2
```

The positions are:

```text
pos[3] = 1
pos[1] = 2
pos[2] = 3
```

Then for every query `x`:

```python
p = pos[x]

vasya += p
petya += n - p + 1
```

Finally print both totals.

---

## Example

Input:

```text
3
3 1 2
3
1 2 3
```

Positions:

```text
Value    Position
1        2
2        3
3        1
```

For query `1`:

```text
Vasya = 2
Petya = 3 - 2 + 1 = 2
```

For query `2`:

```text
Vasya = 3
Petya = 3 - 3 + 1 = 1
```

For query `3`:

```text
Vasya = 1
Petya = 3 - 1 + 1 = 3
```

Totals:

```text
Vasya = 2 + 3 + 1 = 6
Petya = 2 + 1 + 3 = 6
```

Output:

```text
6 6
```

---

## Complexity

Building the position array takes:

```text
O(n)
```

Processing all queries takes:

```text
O(m)
```

Therefore:

```text
Time Complexity: O(n + m)
Space Complexity: O(n)
```

### Important

The answer can become large because there can be up to `10^5` queries and each query can require up to `10^5` comparisons.

In Python this is not a problem because integers automatically support large values.
