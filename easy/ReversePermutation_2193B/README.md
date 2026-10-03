# B. Reverse a Permutation

## Problem

Given a permutation `p` of length `n`, we can reverse exactly one subarray `[l, r]`.

The goal is to obtain the **lexicographically maximum** permutation.

A permutation is lexicographically larger if, at the first position where two permutations differ, it has the larger value.

## Approach

To maximize the permutation lexicographically, we should maximize the **earliest position possible**.

For a permutation of `1...n`, the maximum possible arrangement is:

```text
n, n-1, n-2, ..., 1
```

Find the first position `i` where:

```text
p[i] != n - i
```

The value `n - i` should be placed at position `i`.

Using a position array:

```text
pos[x] = index of x
```

we can find the required value in `O(1)` time.

Let:

```text
j = pos[n - i]
```

Then reverse the segment:

```text
[i, j]
```

This places `n - i` at position `i`, maximizing the earliest position where improvement is possible.

## Algorithm

1. Store the position of every value using `pos`.
2. Find the first index `i` where:

   ```text
   p[i] != n - i
   ```

3. Find the position `j` of `n - i`.
4. Reverse `p[i...j]`.
5. Print the resulting permutation.

If the permutation is already:

```text
n, n-1, ..., 1
```

then no improvement is possible. Reverse a segment of length `1`, which leaves the permutation unchanged.

## Python Implementation

```python
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    # Store the position of each value
    pos = [0] * (n + 1)

    for i in range(n):
        pos[p[i]] = i

    # Find the first incorrect position
    l = -1

    for i in range(n):
        expected = n - i

        if p[i] != expected:
            l = i
            break

    # If an improvement is possible
    if l != -1:
        r = pos[n - l]

        # Reverse p[l...r]
        p[l:r + 1] = p[l:r + 1][::-1]

    print(*p)
```

## Example

### Input

```text
3 2 1 4
```

The first position contains `3`, but the maximum possible value is `4`.

`4` is at index `3`.

Reverse:

```text
3 2 1 4
---------
4 1 2 3
```

Result:

```text
4 1 2 3
```

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The `pos` array allows us to find the required element in `O(1)` instead of searching through the permutation.

## Key Concept

The main idea is **greedy lexicographical maximization**:

> Always maximize the earliest position where the current permutation differs from the ideal descending permutation.

## Tags

`Greedy` `Arrays` `Permutation` `Implementation` `Lexicographical Order`
