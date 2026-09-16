# README — Euclid, Sequence and Two Numbers

## Problem Statement

We are given a sequence `b` of `n` positive integers.

We need to determine whether we can **permute** its elements to form a valid Euclid algorithm sequence:

$$
a_1=x,\quad a_2=y
$$

and

$$
a_{i+2}=a_i \bmod a_{i+1}
$$

for every valid `i`.

If possible, output the first two values:

```text
x y
```

Otherwise, output:

```text
-1
```

---

## Key Observation

The Euclidean algorithm has an important property:

$$
a_{i+2}=a_i\bmod a_{i+1}<a_{i+1}
$$

So after the first two elements, the sequence is **strictly decreasing**.

Therefore, if we sort the given numbers in descending order:

```text
b_sorted = [largest, ..., smallest]
```

the only possible first two elements are:

```text
x = largest
y = second largest
```

Why?

Because every later element must be smaller than the previous element. Hence the first two elements must be the two largest values.

Then we can repeatedly calculate:

```text
remainder = x % y
```

and check whether that remainder exists in the remaining multiset.

If it does, remove it and continue.

---

## Example

Consider:

```text
b = [3, 8, 13, 5]
```

Sort in descending order:

```text
[13, 8, 5, 3]
```

Start with:

```text
x = 13
y = 8
```

Calculate:

```text
13 % 8 = 5
8 % 5 = 3
```

Both `5` and `3` exist in the input.

Therefore:

```text
13 8
```

is a valid answer.

---

## Example Where It Fails

Consider:

```text
b = [1, 2, 3, 4]
```

The first two must be:

```text
4, 3
```

Then:

```text
4 % 3 = 1
```

So far we have:

```text
[4, 3, 1]
```

Next:

```text
3 % 1 = 0
```

But the sequence must contain **positive integers**, and `0` is not allowed.

Also, the remaining `2` cannot be used.

Therefore:

```text
-1
```

---

## Python Solution

```python
import sys
from collections import Counter

input = sys.stdin.readline


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))

        # The first two elements must be the two largest.
        b.sort(reverse=True)

        x = b[0]
        y = b[1]

        # Count remaining elements.
        cnt = Counter(b)

        # Remove x and y.
        cnt[x] -= 1
        cnt[y] -= 1

        possible = True

        while y > 0:
            r = x % y

            # Remainder must be positive.
            if r == 0:
                break

            # Remainder must exist in the input.
            if cnt[r] == 0:
                possible = False
                break

            cnt[r] -= 1

            x, y = y, r

        # All elements must have been used.
        if possible and sum(cnt.values()) == 0:
            print(b[0], b[1])
        else:
            print(-1)


if __name__ == "__main__":
    solve()
```

## Simpler Explanation of the Algorithm

For every test case:

1. Sort the array in descending order.
2. Take the two largest values as `x` and `y`.
3. Calculate:

   ```text
   r = x % y
   
4. Check whether `r` is available in the remaining elements.

5. If yes, remove it and continue with:

   ```text
   x = y
   y = r
   ```

6. If `r == 0` before all elements are used, the answer is `-1`.
7. If every element is successfully used, output the original two largest values.

### Complexity

Sorting takes:

$$
O(n\log n)
$$

The Euclidean algorithm takes approximately:

$$
O(\log(\max b))
$$

So overall:

$$
\boxed{O(n\log n)}
$$

with:

$$
O(n)
$$

extra space for the frequency map.

### Sample Output

For the given input:

```text
1 1
2 1
-1
6 4
13 8
-1
```

The important trick is: **the two largest numbers must be `x` and `y`; after that, simply simulate the Euclidean algorithm and verify that every generated remainder is present.**
