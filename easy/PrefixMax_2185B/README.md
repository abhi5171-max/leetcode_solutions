# B. Prefix Max

## Problem Statement

You are given an array of `n` integers:

\[
a_1,a_2,\ldots,a_n
\]

The **value** of the array is defined as the sum of the maximum element of every prefix:

\[
\text{Value}(a)=\sum_{i=1}^{n}\max(a_1,a_2,\ldots,a_i)
\]

You may swap two elements **at most once**.

The goal is to find the maximum possible value of the array after performing at most one swap.

### Example

For:

```text
[1, 2, 1]
```

The prefix maximums are:

```text
1
2
2
```

Therefore:

\[
1+2+2=5
\]

## Approach

Since:

- `n ≤ 50`
- We are allowed to perform at most one swap.

We can simply try **every possible pair of indices**.

For each pair `(i, j)`:

1. Swap `a[i]` and `a[j]`.
2. Calculate the value of the resulting array.
3. Update the maximum answer.
4. Swap them back.

We also consider the original array, which handles the case where no swap is beneficial.

### Calculating the Prefix Maximum

Maintain a variable `current_max`.

For every element:

```python
current_max = max(current_max, a[i])
```

Add it to the answer:

```python
total += current_max
```

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    def get_value(arr):
        current_max = 0
        total = 0

        for x in arr:
            current_max = max(current_max, x)
            total += current_max

        return total

    # Value without performing a swap
    ans = get_value(a)

    # Try every possible swap
    for i in range(n):
        for j in range(i + 1, n):
            a[i], a[j] = a[j], a[i]

            ans = max(ans, get_value(a))

            # Restore the original array
            a[i], a[j] = a[j], a[i]

    print(ans)
```

## Examples

## Input

```text
4
5
2 1 4 5 3
2
5 1
3
3 2 1
2
6 7
```

### Output

```text
25
10
9
14
```

## Example Explanation

For the first test case:

```text
2 1 4 5 3
```

Swap `2` and `5`:

```text
5 1 4 2 3
```

The prefix maximums become:

```text
5 5 5 5 5
```

Therefore:

\[
5+5+5+5+5=25
\]

So the answer is:

```text
25
```

For the second test case:

```text
5 1
```

The original value is:

\[
5+5=10
\]

Swapping gives:

```text
1 5
```

whose value is:

\[
1+5=6
\]

Therefore, it is better **not to swap**, giving:

```text
10
```

## Correctness

The algorithm checks every possible pair of indices `(i, j)`.

There are only two possibilities:

1. **No swap** — considered by calculating the original array value.
2. **One swap** — every possible pair of indices is tested.

Thus, every valid array obtainable using at most one swap is considered.

For each resulting array, we calculate its exact prefix-maximum sum. Taking the maximum over all these values therefore gives the optimal answer.

## Complexity

There are:

\[
O(n^2)
\]

possible swaps.

Calculating the value of an array takes:

\[
O(n)
\]

Therefore:

\[
\boxed{O(n^3)}
\]

per test case.

Since `n ≤ 50`, this is easily fast enough.

### Space Complexity

\[
\boxed{O(1)}
\]

extra space, excluding the input array.

## Key Idea

> Since `n` is small, try every possible swap and calculate the prefix maximum sum.

This brute-force approach is simple, reliable, and fits comfortably within the constraints.
