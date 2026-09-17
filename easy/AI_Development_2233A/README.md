# AI Project Development

## Problem

Maxim and Nikita are working on a project containing `n` lines of code.

* Maxim writes `x` lines per hour from the beginning.
* Nikita can either:

  1. Start writing immediately at `y` lines per hour, or
  2. Spend `z` hours setting up an AI agent and then write at `10 × y` lines per hour.

During AI setup, Nikita writes nothing, but Maxim continues writing at `x` lines per hour.

The project finishes as soon as at least `n` lines have been written.

Since time is measured in **full hours**, we use the ceiling of the required time.

We need to find the minimum completion time if Nikita chooses optimally.

---

## Approach

We calculate the completion time for both choices.

### 1. Without AI

Both people start working immediately.

Their combined speed is:

```text
x + y
```

Therefore, the required number of hours is:

```text
ceil(n / (x + y))
```

Using integer arithmetic:

```python
(n + x + y - 1) // (x + y)
```

---

### 2. With AI

Nikita spends `z` hours setting up the AI.

During these `z` hours, only Maxim works:

```text
lines_written = x × z
```

There are two cases.

#### Case A: Project finishes during AI setup

If:

```text
x × z >= n
```

then Maxim alone completes the project before AI setup ends.

So the completion time is:

```text
ceil(n / x)
```

#### Case B: Project is not finished during setup

After `z` hours, the remaining work is:

```text
remaining = n - x × z
```

Now both work together:

* Maxim: `x` lines/hour
* Nikita: `10y` lines/hour

Combined speed:

```text
x + 10y
```

Additional required hours:

```text
ceil(remaining / (x + 10y))
```

Therefore:

```text
AI time = z + ceil(remaining / (x + 10y))
```

---

## Final Answer

Nikita chooses the faster option:

```text
answer = min(time_without_ai, time_with_ai)
```

---

## Python 3 Solution

```python
import sys


def ceil_div(a, b):
    return (a + b - 1) // b


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, x, y, z = map(int, input().split())

        # Option 1: No AI
        without_ai = ceil_div(n, x + y)

        # Option 2: Use AI
        # Maxim works alone during AI setup.
        if x * z >= n:
            with_ai = ceil_div(n, x)
        else:
            remaining = n - x * z
            with_ai = z + ceil_div(remaining, x + 10 * y)

        print(min(without_ai, with_ai))


if __name__ == "__main__":
    solve()
```

## Example

### Input

```text
10
1 1 1 1
2 1 1 5
3 1 1 1
110 10 9 1
54 14 1 1
30 8 1 13
6 2 1 3
82 4 5 7
200 3 2 4
76 211 743 432
```

### Output

```text
1
1
2
2
3
4
2
8
13
1
```

---

## Complexity

For each test case, we perform only a constant number of calculations.

* **Time Complexity:** `O(1)` per test case
* **Total Time Complexity:** `O(t)`
* **Space Complexity:** `O(1)`

With `t ≤ 100`, this easily fits within the limits.

## Key Formula

```text
Without AI:
ceil(n / (x + y))

With AI:
if x × z >= n:
    ceil(n / x)
else:
    z + ceil((n - x × z) / (x + 10y))

Answer:
min(without_ai, with_ai)
```
