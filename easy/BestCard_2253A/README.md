# A. The Best Card

## Problem

There are `n` cards with values:

```text
2, 3, 4, ..., n + 1
```

To determine the winner between two cards with values `x` and `y`:

* If one number is divisible by the other, the card with the **smaller value wins**.
* Otherwise, the card with the **larger value wins**.

We need to determine whether there exists a card that wins against **every other card**.

---

## Observation

Consider the largest card, `n + 1`.

### When `n + 1` is Prime

A prime number is not divisible by any smaller number greater than `1`.

Therefore, for every other card:

* Neither card divides the other.
* The larger card wins.

Since `n + 1` is the largest card, it wins against every other card.

So the answer is:

```text
YES
```

### When `n + 1` is Composite

A composite number has a divisor `d` such that:

```text
2 <= d < n + 1
```

Since `n + 1` is divisible by `d`, according to the rules, the smaller card `d` wins against `n + 1`.

Therefore, the largest card cannot win against every card, and no suitable card exists.

So the answer is:

```text
NO
```

---

## Algorithm

For each test case:

1. Check whether `n + 1` is prime.
2. If it is prime, print `YES`.
3. Otherwise, print `NO`.

---

## Python Solution

```python
import sys


def is_prime(x):
    if x < 2:
        return False

    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1

    return True


input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    if is_prime(n + 1):
        print("YES")
    else:
        print("NO")
```

---

## Complexity Analysis

### Time Complexity

For each test case:

```text
O(√n)
```

### Space Complexity

```text
O(1)
```

---

## Example

### Input

```text
5
2
3
4
5
8
```

### Output

```text
YES
NO
YES
NO
NO
```

---

## Key Takeaway

The answer is `YES` **if and only if `n + 1` is a prime number**.
