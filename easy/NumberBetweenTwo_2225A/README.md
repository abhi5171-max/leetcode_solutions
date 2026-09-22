# Codeforces — A. A Number Between Two Others

## Problem

You are given two integers `x` and `y` such that:

* `y > x`
* `y` is divisible by `x`

You need to determine whether there exists an integer `z` such that:

1. `x < z < y`
2. `z` is divisible by `x`
3. `y` is **not** divisible by `z`

Print `YES` if such a `z` exists; otherwise, print `NO`.

---

## Approach

Since `y` is divisible by `x`, we can write:

$$
y = x \times k
$$

where:

$$
k = \frac{y}{x}
$$

Any number `z` divisible by `x` can be written as:

$$
z = x \times d
$$

For `z` to lie strictly between `x` and `y`:

$$
1 < d < k
$$

If `k = 2`, there is no integer `d` satisfying this condition, so the answer is:

```text
NO
```

For every `k > 2`, a suitable value of `z` always exists.

Therefore, the condition becomes:

$$
\frac{y}{x} > 2
$$

So:

* If `y / x > 2` → `YES`
* Otherwise → `NO`

---

## Algorithm

For each test case:

1. Read `x` and `y`.
2. Calculate `y // x`.
3. If `y // x > 2`, print `YES`.
4. Otherwise, print `NO`.

---

## Complexity

* **Time Complexity:** `O(t)`
* **Space Complexity:** `O(1)`

where `t` is the number of test cases.

---

## Python Code

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        x, y = map(int, input().split())

        if y // x > 2:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
```

---

## Example

### Input

```text
5
1 2
1 3
1234567890 12345678900
2 8
7 84
```

### Output

```text
NO
YES
YES
YES
YES
```

---

## Key Takeaway

The important observation is that because `y` is already a multiple of `x`, we only need to consider the ratio:

$$
k = \frac{y}{x}
$$

The answer is `NO` only when the ratio is `2`; for every ratio greater than `2`, a valid `z` exists.
