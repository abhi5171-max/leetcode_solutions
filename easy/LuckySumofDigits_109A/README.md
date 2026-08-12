# A. Lucky Sum of Digits

## Problem

A lucky number is a positive integer whose decimal representation contains only the digits **4** and **7**.

Given an integer `n`, find the **minimum lucky number** whose digits have a sum equal to `n`.

If no such lucky number exists, print `-1`.

## Approach

Suppose the required lucky number contains:

* `a` digits equal to `4`
* `b` digits equal to `7`

Then its digit sum must satisfy:

[
4a + 7b = n
]

We try every possible number of `7`s and determine whether the remaining sum can be formed using `4`s.

For every valid combination, we construct:

```text
444...777
```

A number with fewer digits is always smaller than a number with more digits. Therefore, we select the valid candidate with the minimum length.

For the same length, placing all `4`s before `7`s gives the smallest number.

## Algorithm

1. Read `n`.
2. Try every possible count `b` of digit `7`.
3. Calculate:
   [
   remaining = n - 7b
   ]
4. If `remaining` is non-negative and divisible by `4`, calculate the number of `4`s.
5. Construct the candidate using:

   * `a` copies of `4`
   * `b` copies of `7`
6. Keep the candidate with the smallest length.
7. If no candidate exists, print `-1`.

## Complexity

* **Time:** (O(n))
* **Space:** (O(n)) in the worst case for constructing the result.

Since (n \le 10^6), this approach is easily fast enough.

## Example 1

### Input

```text
11
```

### Output

```text
47
```

Because:

[
4 + 7 = 11
]

Therefore, `47` is a lucky number with digit sum `11`.

## Example 2

### Input

```text
10
```

### Output

```text
-1
```

There is no combination of `4`s and `7`s whose sum is `10`.

## Language

**Python 3**
