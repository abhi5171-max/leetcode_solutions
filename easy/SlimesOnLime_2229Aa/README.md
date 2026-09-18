# A. Slimes on a Line — Python 3

## Approach

In one operation, choosing `x` moves every slime **one step toward `x`**:

* If `a[i] < x`, it increases by `1`.
* If `a[i] > x`, it decreases by `1`.
* If `a[i] == x`, it stays there.

To make all slimes meet, the optimal target is a position around the **middle of the sorted array**.

For a chosen target `x`, the number of operations needed is:

$$
\max_i |a_i-x|
$$

So we need to minimize the maximum distance to the target. This is achieved by choosing the midpoint between the minimum and maximum positions.

Therefore:

$$
\boxed{\left\lceil\frac{\max(a)-\min(a)}{2}\right\rceil}
$$

which can be calculated using integer arithmetic as:

```python
(maximum - minimum + 1) // 2
```

### Complexity

* **Time:** `O(n)` per test case
* **Space:** `O(n)` for storing the array

---

## Problem

There are `n` slimes placed at different positions on a line.

In one operation, we choose an integer position `x`. Then:

* A slime to the left of `x` moves one position right.
* A slime to the right of `x` moves one position left.
* A slime already at `x` does not move.

We need to find the minimum number of operations required to make all slimes occupy the same position.

## Key Observation

In every operation, each slime moves at most one position toward the selected target.

Let:

* `mn` = minimum position
* `mx` = maximum position

The farthest two slimes are `mx - mn` positions apart.

If we choose a target approximately in the middle, both extreme slimes move toward it. Therefore, the minimum number of operations is half of the distance between the minimum and maximum positions, rounded up.

### Formula

```text
answer = ceil((max_position - min_position) / 2)
```

Using integer arithmetic:

```python
(max_position - min_position + 1) // 2
```

## Example

For:

```text
1 2 3 4 5
```

The minimum position is `1` and the maximum position is `5`.

```text
distance = 5 - 1 = 4
answer = ceil(4 / 2) = 2
```

We can choose `x = 3` twice:

```text
1 2 3 4 5
↓
2 3 3 3 4
↓
3 3 3 3 3
```

So the answer is `2`.

## Python 3 Solution

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        mn = min(a)
        mx = max(a)

        ans = (mx - mn + 1) // 2

        print(ans)


if __name__ == "__main__":
    solve()
```

## Complexitys

For each test case:

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

Since the sum of `n` over all test cases is at most `1000`, this easily fits within the limits.

## Important Insight

Only the **minimum and maximum positions** matter.

The answer does not depend on how many slimes are between them:

```text
answer = ceil((max(a) - min(a)) / 2)
```
