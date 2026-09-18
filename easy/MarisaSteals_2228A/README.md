
# A. Marisa Steals Reimu's Takeout

## Problem

We are given a sequence `w` containing only the values `0`, `1`, and `2`.

In one operation, we can choose any **non-empty subsequence** whose sum is divisible by `3` and remove it.

We need to find the **maximum number of operations** that can be performed.

---

## Key Observation

There are three types of useful subsequences:

### 1. Single `0`

Since:

```text
0 % 3 = 0
```

Every `0` can be removed individually.

So if there are `count0` zeros, they always contribute:

```text
count0
```

operations.

### 2. A `1` and a `2`

Their sum is:

```text
1 + 2 = 3
```

which is divisible by `3`.

Therefore, we can remove one `1` and one `2` together.

If there are `count1` ones and `count2` twos, we can perform:

```text
min(count1, count2)
```

such operations.

### 3. Three `1`s or three `2`s

We could also remove:

```text
1 + 1 + 1 = 3
```

or:

```text
2 + 2 + 2 = 6
```

However, using three equal elements gives only **one operation**, while pairing a `1` with a `2` also gives one operation using only two elements.

The important strategy is to maximize the number of groups, so we should pair as many `1`s and `2`s as possible first.

After that, the remaining elements are all of the same type.

For three remaining `1`s, we can perform one operation.

Similarly, for three remaining `2`s, we can perform one operation.

Thus:

```text
answer =
count0
+ min(count1, count2)
+ (remaining1 // 3)
+ (remaining2 // 3)
```

where:

```text
remaining1 = count1 - min(count1, count2)
remaining2 = count2 - min(count1, count2)
```

---

## Example

Consider:

```text
1 2 1 2 1
```

Counts:

```text
count1 = 3
count2 = 2
count0 = 0
```

We can pair two `1`s with two `2`s:

```text
(1 + 2) → operation 1
(1 + 2) → operation 2
```

One `1` remains.

Therefore:

```text
answer = 2
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
        w = list(map(int, input().split()))

        count0 = w.count(0)
        count1 = w.count(1)
        count2 = w.count(2)

        # Every zero can be removed individually.
        ans = count0

        # Pair 1 and 2: 1 + 2 = 3.
        pairs = min(count1, count2)
        ans += pairs

        count1 -= pairs
        count2 -= pairs

        # Three 1s or three 2s have sums divisible by 3.
        ans += count1 // 3
        ans += count2 // 3

        print(ans)


if __name__ == "__main__":
    solve()
```

## Complexity

For each test case:

* **Time:** `O(n)`
* **Space:** `O(n)`

With `n ≤ 100` and at most `500` test cases, this easily fits within the limits.

## Summary

The main idea is:

1. Remove every `0` individually.
2. Pair as many `1`s and `2`s as possible because `1 + 2 = 3`.
3. Group any remaining `1`s or `2`s into groups of three.

```text
Answer = count0
       + min(count1, count2)
       + remaining1 // 3
       + remaining2 // 3
```
