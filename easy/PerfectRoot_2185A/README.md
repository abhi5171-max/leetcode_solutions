# A. Perfect Root

## Problem Statement

A positive integer is called a **perfect root** if there exists an integer \(x\) such that:

\[
n = x^2
\]

For each test case, we need to output \(n\) distinct perfect roots.

Since every perfect square is a perfect root, we can simply generate:

\[
1^2, 2^2, 3^2, \ldots, n^2
\]

These values are guaranteed to be distinct.

## Approach

For each test case:

1. Read the value of `n`.
2. Iterate from `1` to `n`.
3. Calculate `i²` for every `i`.
4. Print the generated perfect squares.

For example, if `n = 5`:

```text
1 4 9 16 25
```

All five values are distinct perfect roots.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())

    for i in range(1, n + 1):
        print(i * i, end=" ")

    print()
```

## Example

### Input

```text
3
1
2
5
```

### Output

```text
1
1 4
1 4 9 16 25
```

## Correctness

For every integer `i` from `1` to `n`, the value:

```text
i * i
```

is a perfect square and therefore a perfect root.

Also, if `i ≠ j`, then:

\[
i^2 \ne j^2
\]

for positive integers `i` and `j`. Hence, all generated values are distinct.

Therefore, the algorithm always produces exactly `n` distinct perfect roots.

## Complexity

For each test case:

- **Time:** `O(n)`
- **Space:** `O(1)` excluding output storage.

## Key Concept

> To generate `n` distinct perfect roots, simply output the first `n` perfect squares.

```text
1², 2², 3², ..., n²
```
