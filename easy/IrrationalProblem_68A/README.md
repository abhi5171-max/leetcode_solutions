# A. Irrational Problem

## Problem

Little Petya is given four distinct integers and an integer range `[a, b]`.

The function `f(x)` is created by taking the remainder of `x` successively with the four given numbers. Since Petya forgot the order of the numbers, all `4! = 24` permutations are equally likely.

For a number `x`, we need to determine whether there are **at least 7 permutations** for which:

```text
f(x) = x
```

Finally, count how many integers `x` in `[a, b]` satisfy this condition.

## Approach

There are only 24 possible orders of the four numbers.

For every `x` from `a` to `b`:

1. Generate all 24 permutations of the four numbers.
2. For each permutation, calculate:

   ```text
   (((x % p1) % p2) % p3) % p4
   ```
3. Count the permutations for which the final value is equal to `x`.
4. If the count is at least `7`, add `x` to the answer.

Since `b ≤ 31415`, a direct brute-force solution is fast enough.

## Algorithm

```text
answer = 0

Generate all 24 permutations

for x from a to b:
    count = 0

    for every permutation:
        value = x

        for every number in the permutation:
            value = value % number

        if value == x:
            count++

    if count >= 7:
        answer++

print answer
```

## Complexity

There are at most `31416` values and `24` permutations.

* **Time Complexity:** `O((b-a+1) × 24 × 4)`
* **Space Complexity:** `O(24)`

This easily fits within the given limits.

## Python 3 Solution

```python
import sys
from itertools import permutations


def main():
    p = list(map(int, sys.stdin.readline().split()))

    p1, p2, p3, p4, a, b = p
    nums = [p1, p2, p3, p4]

    perms = list(permutations(nums))

    answer = 0

    for x in range(a, b + 1):
        count = 0

        for perm in perms:
            value = x

            for mod in perm:
                value %= mod

            if value == x:
                count += 1

        if count >= 7:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
```

## Key Concept

The important observation is that the number of permutations is fixed at only `24`. Therefore, brute force over every permutation and every `x` is completely feasible.

## Tags

`Brute Force` `Permutations` `Modular Arithmetic` `Implementation` `Codeforces`
