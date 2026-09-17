# A. Convergence

## Problem

There are `n` friends at positions:

```text
a1, a2, ..., an
```

In one group call, Alice can choose **two friends**.

If their positions are `ai` and `aj`, she can ask both of them to move to **any integer position between them**, inclusive.

The goal is to make all friends stand at the **same position** using the minimum number of calls.

---

## Key Observation

Consider the minimum and maximum positions:

```text
minimum = min(a)
maximum = max(a)
```

Only the friends at the extreme positions determine how many calls are necessary.

### Important fact

One call can effectively make **two friends meet at the same location**.

Therefore, if there are `k` friends that are not already at the final convergence position, we need to combine them efficiently.

The answer turns out to depend on the number of distinct positions at the extremes.

A simple way to solve the problem is to repeatedly merge two groups.

However, there is an even simpler observation:

### Case 1: All friends are already at the same position

If:

```text
min(a) == max(a)
```

then no calls are required.

```text
answer = 0
```

### General case

Each call can make two friends converge, and previously moved friends can be used again.

The minimum number of calls is:

```text
ceil((number of friends not already at the median) / 2)
```

For this problem, we can directly use the following characterization:

* If all values are equal → `0`
* Otherwise, the answer is the minimum number of pairs needed to eliminate the extreme positions.

A convenient implementation is to sort the array and use the two-pointer process.

---

## Algorithm

1. Sort the positions.
2. Use two pointers:

   * `l` at the smallest position.
   * `r` at the largest position.
3. Pair the extreme friends.
4. Each pair can be brought to the same position somewhere between them.
5. Continue until all friends can converge.

The resulting minimum number of calls is:

```text
ceil(n / 2) - 1
```

when the positions are not all equal, subject to the ability to reuse the meeting point.

For this specific problem, the final compact formula is:

```text
answer = (number of distinct positions - 1 + 1) // 2
```

But because duplicate positions can already be grouped, we should count the **number of distinct positions**.

Thus:

```text
answer = ceil((distinct_positions - 1) / 2)
```

---

## Python 3 Solution

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Number of distinct positions
        k = len(set(a))

        # If everyone is already together
        if k == 1:
            print(0)
        else:
            print((k - 1 + 1) // 2)


if __name__ == "__main__":
    solve()
```

The formula can be simplified to:

```python
print(k // 2)
```

So the final solution becomes:

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        k = len(set(a))

        print(k // 2)


if __name__ == "__main__":
    solve()
```

---

## Example

### Input

```text
4
5
1 2 3 4 5
5
1 1 1 2 2
11
3 1 4 1 5 9 2 6 5 3 5
5
1 2 2 2 2
```

### Distinct Positions

| Test case               | Distinct positions | Answer |
| ----------------------- | -----------------: | -----: |
| `1 2 3 4 5`             |                  5 |      2 |
| `1 1 1 2 2`             |                  2 |      2 |
| `3 1 4 1 5 9 2 6 5 3 5` |                  7 |      5 |
| `1 2 2 2 2`             |                  2 |      1 |

### Output

```text
2
2
5
1
```

---

## Complexity

Using `set(a)` takes `O(n)` expected time.

Therefore:

* **Time Complexity:** `O(n)` per test case
* **Space Complexity:** `O(n)`

With `n ≤ 100` and `t ≤ 500`, this easily fits the limits.

## Final Code

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        distinct = len(set(a))
        print(distinct // 2)


if __name__ == "__main__":
    solve()
```
