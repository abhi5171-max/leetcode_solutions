# Codeforces — A. Flip Flops

## Problem

OtterZ has combat power `c` and `n` monsters with powers `a[i]`.

For each monster, he can:

* Kill it if `a[i] <= c`, after which `c += a[i]`.
* Use a flip-flop to increase its power by `1`.

The goal is to maximize the final combat power.

## Observation

Killing a monster is always beneficial because it increases `c`.

If a monster currently has power greater than `c`, increasing its power using a flip-flop only makes it harder to kill.

Therefore, we should first focus on monsters that are already killable.

Sort the monster powers in increasing order. Then process them:

```text
if a[i] <= c:
    c += a[i]
else:
    stop
```

Once we encounter a monster with `a[i] > c`, all later monsters are at least as large, so none of them can currently be killed either.

## Algorithm

For each test case:

1. Read `n`, `c`, and `k`.
2. Sort the array `a`.
3. Iterate through the sorted array.
4. If `a[i] <= c`, kill the monster and update:
   `c = c + a[i]`.
5. Otherwise, stop.
6. Print `c`.

## Complexity

Sorting takes:

`O(n log n)`

The scan takes:

`O(n)`

Therefore:

**Time:** `O(n log n)`

**Space:** `O(n)`

## Python Code

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, c, k = map(int, input().split())
        a = sorted(map(int, input().split()))

        for x in a:
            if x <= c:
                c += x
            else:
                break

        print(c)


if __name__ == "__main__":
    solve()
```
