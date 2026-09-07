# A. Little Elephant and Function

## Problem Description

Given a permutation of integers from `1` to `n`, we need to find a permutation such that after calling the recursive function `f(n)`, the permutation becomes sorted in ascending order.

The function works as follows:

```text
f(x):
    if x == 1:
        return

    f(x - 1)
    swap(a[x - 1], a[x])
```

## Approach

Let's understand what happens when we call `f(n)`.

For example, for `n = 4`, the swaps happen in this order:

```text
swap(a1, a2)
swap(a2, a3)
swap(a3, a4)
```

Consider the array:

```text
[a1, a2, a3, a4]
```

After the swaps:

```text
[a2, a3, a4, a1]
```

So, the function effectively moves the **first element to the last position** and shifts all other elements one position to the left.

We want the final permutation to be:

```text
1 2 3 ... n
```

Therefore, the initial permutation should be:

```text
n 1 2 3 ... n-1
```

After applying the function:

```text
n 1 2 3 ... n-1
↓
1 2 3 ... n
```

## Algorithm

1. Read integer `n`.
2. Print `n` as the first element.
3. Print all integers from `1` to `n - 1`.

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` for storing the output list.

## Python 3 Solution

```python
s
```

## Example

### Input

```text
4
```

### Output

```text
4 1 2 3
```

After calling `f(4)`:

```text
4 1 2 3
→ 1 2 3 4
```

Thus, the permutation becomes sorted successfully.
