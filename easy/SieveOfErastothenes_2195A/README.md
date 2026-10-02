# A. Sieve of Eratosthenes

## Problem Statement

You are given `n` positive integers. Determine whether it is possible to select one or more elements such that their product is exactly `67`.

### Constraints

* `1 ≤ t ≤ 10⁴`
* `1 ≤ n ≤ 5`
* `1 ≤ aᵢ ≤ 67`

## Approach

The important observation is that **67 is a prime number**.

For the product of selected positive integers to be exactly `67`:

* We must select `67`.
* Any additional selected elements can only be `1`, since multiplying by any number greater than `1` would make the product greater than `67`.

Therefore, the answer is:

* `YES` if the array contains `67`.
* `NO` otherwise.

## Algorithm

For each test case:

1. Read `n`.
2. Read the `n` elements.
3. Check whether `67` exists in the array.
4. If found, print `YES`.
5. Otherwise, print `NO`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if 67 in a:
        print("YES")
    else:
        print("NO")
```

## Example

### Input

```text
2
5
1 7 6 7 67
5
1 3 5 7 8
```

### Output

```text
YES
NO
```

## Complexity

* **Time Complexity:** `O(n)` per test case
* **Space Complexity:** `O(n)` for storing the array

## Key Takeaway

Since `67` is prime, a product of positive integers can equal `67` only when one of the selected elements is `67` and all other selected elements, if any, are `1`.
