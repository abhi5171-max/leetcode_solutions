# Friendly Numbers

## Problem

For an integer `x`, another integer `y` is called **friendly** if:

$$
y - d(y) = x
$$

where `d(y)` is the sum of the digits of `y`.

For each given `x`, find the number of friendly integers `y`.

## Approach

We need to find all `y` satisfying:

```text
y - digit_sum(y) = x
```

The digit sum of an integer is relatively small. Since `x ≤ 10^9`, checking the next `100` numbers is sufficient.

For every:

```text
y = x + 1, x + 2, ..., x + 100
```

calculate:

```text
y - digit_sum(y)
```

If it equals `x`, increase the answer.

### Why only 100 numbers?

For numbers in the given range, the sum of their digits is much smaller than `100`. Therefore, if:

```text
y - digit_sum(y) = x
```

then `y` cannot be more than a small constant distance from `x`. Checking 100 consecutive values safely covers all possibilities.

## Example

For:

```text
x = 18
```

The friendly numbers are:

```text
20, 21, 22, ..., 29
```

For example:

```text
20 - (2 + 0) = 18
25 - (2 + 5) = 18
29 - (2 + 9) = 18
```

Therefore:

```text
Answer = 10
```

For `x = 1`, there are no friendly numbers.

## Python Solution

```python
import sys


def digit_sum(n):
    return sum(map(int, str(n)))


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        x = int(input())

        ans = 0

        for y in range(x + 1, x + 101):
            if y - digit_sum(y) == x:
                ans += 1

        print(ans)


if __name__ == "__main__":
    solve()
```

## Example Input

```text
3
1
18
998244360
```

## Example Output

```text
0
10
10
```

For `998244360`, the 10 friendly numbers are:

```text
998244400
998244401
998244402
998244403
998244404
998244405
998244406
998244407
998244408
998244409
```

## Complexity

For each test case, only 100 numbers are checked.

* **Time:** `O(100 × D)` ≈ `O(D)`
* **Space:** `O(1)`

where `D` is the number of digits in `x`.

## Tags

`Codeforces` `Python` `Implementation` `Math` `Digit Sum` `Brute Force`
