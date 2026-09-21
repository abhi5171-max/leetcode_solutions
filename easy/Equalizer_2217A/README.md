# A. The Equalizer

## Problem

We have an array of `n` positive integers. Shaunak goes first.

On every normal turn, a player chooses an element `a[i] > 0` and decreases it by `1`.

Shaunak also has a **special move**, which he can use at most once:

```text
a[i] = k   for every i
```

The player who makes the last move wins.

We need to determine whether Shaunak can always win with optimal play.

---

## Approach

Let:

$$
S = a_1+a_2+\dots+a_n
$$

Without using the special move, the game has exactly `S` normal moves because every normal move decreases the total sum by exactly `1`.

Therefore:

* If `S` is **odd**, Shaunak makes the last move → **YES**
* If `S` is **even**, Yash makes the last move → **NO**

Now consider Shaunak's special move.

When he uses it, every element becomes `k`, so the new total number of remaining normal moves is:

$$
n \times k
$$

After Shaunak uses the special move, **Yash gets the next turn**.

Therefore:

* If `n × k` is **even**, Shaunak makes the last normal move → **YES**
* If `n × k` is **odd**, Yash makes the last normal move → the special move does not help.

So Shaunak wins if **either**:

$$
S \text{ is odd}
$$

or

$$
n\times k \text{ is even}
$$

### Final Condition

```text
YES if (sum(a) % 2 == 1) OR (n * k % 2 == 0)
NO otherwise
```

---

## Algorithm

For every test case:

1. Read `n` and `k`.
2. Calculate the sum of all elements.
3. Check whether the sum is odd.
4. Check whether `n * k` is even.
5. If either condition is true, print `YES`.
6. Otherwise, print `NO`.

---

## Python Solution

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        total = sum(a)

        if total % 2 == 1 or (n * k) % 2 == 0:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
```

---

## Example

For:

```text
n = 3
k = 2
a = [3, 3, 3]
```

Sum:

$$
3+3+3=9
$$

`9` is odd, so Shaunak can already win without needing the special move.

Also:

$$
n\times k=3\times2=6
$$

which is even, so using the special move can also lead to a win.

Therefore:

```text
YES
```

---

## Complexity

For each test case:

* **Time:** `O(n)`
* **Space:** `O(n)` for storing the array

The calculation itself after reading the array is `O(1)`.

---

## Key Idea

> **Normal game:** Shaunak wins when `sum(a)` is odd.
> **Special move:** Shaunak wins when `n × k` is even.
> Therefore:

```text
if sum(a) is odd OR n*k is even:
    YES
else:
    NO
```
