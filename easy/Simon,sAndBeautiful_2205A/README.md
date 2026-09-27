# Codeforces 2205A — Simons and Making It Beautiful

## Problem

Given a permutation `p` of length `n`, an index `i` is called **ugly** if:

$$
p_1,p_2,\ldots,p_i
$$

has maximum value equal to `i`.

You may perform **at most one swap** between two positions. The goal is to minimize the number of ugly indices.

## Approach

The largest value in the permutation is always `n`.

Therefore, for index `n`:

$$
\max(p_1,\ldots,p_n)=n
$$

so index `n` is always ugly.

Hence, the minimum possible number of ugly indices is at least **1**.

To achieve exactly one ugly index:

1. Find the position of `n`.
2. Swap `n` with the first element.
3. Now `n` is at position `1`.
4. For every index `i < n`, the prefix already contains `n`, so its maximum is `n`, which cannot equal `i`.
5. At `i = n`, the prefix maximum is `n`, so exactly one index is ugly.

Thus, this construction is always optimal.

## Algorithm

```text
Find the position of n
Swap p[0] and p[position_of_n]
Print the resulting permutation
```

## Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        pos = a.index(n)

        a[0], a[pos] = a[pos], a[0]

        print(*a)


if __name__ == "__main__":
    solve()
```

## Complexity

* **Time:** `O(n)` per test case
* **Space:** `O(n)` for storing the permutation

## Key Insight

The important observation is that **`n` is unavoidable as an ugly index**. By moving `n` to the first position, we ensure that every other prefix has maximum `n`, preventing any index before `n` from being ugly.

Therefore, the answer always contains exactly **one ugly index**, which is the minimum possible.

## Example

### Input

```text
5
2
1 2
4
2 3 1 4
5
3 2 4 5 1
1
1
8
4 1 3 2 6 7 8 5
```

### One Valid Output

```text
2 1
4 3 1 2
5 2 4 3 1
1
8 1 3 2 6 7 4 5
```

Any permutation obtained using at most one swap that has the minimum number of ugly indices is accepted.
