# A. Bicycle Chain

## Problem

Vasya has:

* `n` stars on the pedal axle, with tooth counts `a[i]`
* `m` stars on the rear wheel axle, with tooth counts `b[j]`

For a pair of stars `(i, j)`, the gear ratio is:

$$
\frac{b[j]}{a[i]}
$$

Vasya wants to consider only gears whose ratio is an **integer**.

Among all such gears, he wants the ones with the **maximum integer ratio**.

The task is to find how many gears have this maximum ratio.

## Key Observation

For every pair `(a[i], b[j])`:

* The ratio is an integer if `b[j] % a[i] == 0`.
* If it is an integer, calculate:

$$
ratio = \frac{b[j]}{a[i]}
$$

We keep track of:

1. The maximum integer ratio found so far.
2. The number of pairs having that ratio.

If a larger ratio is found, reset the count to `1`.

If the same maximum ratio is found again, increase the count.

Since `n, m ≤ 50`, checking every possible pair is fast enough.

## Algorithm

1. Read `n` and array `a`.
2. Read `m` and array `b`.
3. Initialize:

   * `max_ratio = 0`
   * `count = 0`
4. For every `a[i]` and `b[j]`:

   * Check whether `b[j]` is divisible by `a[i]`.
   * If yes, calculate `ratio = b[j] // a[i]`.
   * If `ratio > max_ratio`:

     * Update `max_ratio`.
     * Set `count = 1`.
   * If `ratio == max_ratio`:

     * Increment `count`.
5. Print `count`.

## Python 3 Solution

```python
n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

max_ratio = 0
count = 0

for x in a:
    for y in b:
        if y % x == 0:
            ratio = y // x

            if ratio > max_ratio:
                max_ratio = ratio
                count = 1
            elif ratio == max_ratio:
                count += 1

print(count)
```

## Example 1

### Input

```text
2
4 5
3
12 13 15
```

Valid integer ratios are:

```text
12 / 4 = 3
15 / 5 = 3
```

The maximum ratio is `3`, and it occurs **2 times**.

### Output

```text
2
```

## Example 2

### Input

```text
4
1 2 3 4
5
10 11 12 13 14
```

The maximum integer ratio is:

```text
14 / 2 = 7
```

It occurs only once.

### Output

```text
1
```

## Complexity

There are `n × m` possible pairs.

* **Time Complexity:** `O(n × m)`
* **Space Complexity:** `O(n + m)` for storing the two arrays.

With `n, m ≤ 50`, this easily fits within the limits.
