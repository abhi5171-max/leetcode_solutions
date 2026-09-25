# A. 1-1

## Problem

You are given a binary string `s` of length `n`.

In one move, you can choose a position `i` (`2 ≤ i ≤ n-1`) such that:

```text
s[i-1] = s[i+1] = 1
```

and change `s[i]` to either `0` or `1`.

Find:

* The **minimum** possible number of `1`s.
* The **maximum** possible number of `1`s.

---

## 💡 Key Observation

The operation only affects positions that have `1` on both sides.

We can analyze consecutive runs of `1`s and `0`s.

### Minimum Number of 1s

For a consecutive run of `1`s with length `L`, we can change some internal `1`s to `0`s.

The minimum number of `1`s that remain is:

$$
\left\lceil\frac{L+1}{2}\right\rceil
$$

In integer arithmetic:

```text
(L + 2) // 2
```

For example:

```text
11111 → 10101
```

So a run of length `5` contributes `3` ones.

---

### Maximum Number of 1s

A `0` can be changed to `1` only when it has `1`s on both sides:

```text
101 → 111
```

Therefore, every zero-run of length exactly `1` that is surrounded by `1`s can be converted into `1`.

Example:

```text
011011
   ↑
```

The isolated `0` between two `1`s can be changed to `1`.

So:

```text
maximum = initial_ones + number_of_convertible_single_zero_runs
```

---

## 🧠 Algorithm

For every test case:

1. Count the initial number of `1`s.
2. Traverse the string.
3. For every consecutive `1`-run of length `L`:

   * Add `(L + 2) // 2` to the minimum.
4. For every zero-run:

   * If its length is `1` and it is surrounded by `1`s, increment the maximum.
5. Print `minimum` and `maximum`.

---

## 💻 Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()

        minimum = 0
        maximum = s.count('1')

        i = 0

        while i < n:
            if s[i] == '1':
                j = i

                while j < n and s[j] == '1':
                    j += 1

                length = j - i

                # Minimum contribution of this 1-run
                minimum += (length + 2) // 2

                i = j

            else:
                j = i

                while j < n and s[j] == '0':
                    j += 1

                length = j - i

                # A single zero between two 1s can become 1
                if length == 1 and i > 0 and j < n:
                    maximum += 1

                i = j

        print(minimum, maximum)


if __name__ == "__main__":
    solve()
```

---

## 🔍 Example

### Input

```text
4
3
111
6
011011
7
1011101
9
100101101
```

### Output

```text
2 3
3 5
4 7
5 7
```

For example:

```text
111 → 101
```

gives the minimum `2`, while doing nothing gives the maximum `3`.

---

## ⏱️ Complexity

For each test case, the string is traversed only once.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## 📌 Key Takeaway

```text
Minimum:
For every 1-run of length L → (L + 2) // 2

Maximum:
Initial number of 1s
+ isolated 0s surrounded by 1s
```

The solution depends only on the lengths of consecutive runs in the binary string.
