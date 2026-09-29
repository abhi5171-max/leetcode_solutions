# A. Parkour Design

## Problem

Steve can perform only three types of moves on the coordinate plane:

* `(x, y) → (x + 2, y + 1)`
* `(x, y) → (x + 3, y)`
* `(x, y) → (x + 4, y - 1)`

Given a target coordinate `(x, y)`, determine whether it is possible to start from `(0, 0)` and reach `(x, y)` using only these moves.

## Approach

Let:

* `a` = number of `(2, +1)` moves
* `b` = number of `(3, 0)` moves
* `c` = number of `(4, -1)` moves

Then:

```text
x = 2a + 3b + 4c
y = a - c
```

### Case 1: `y >= 0`

Since:

```text
a = c + y
```

Substituting into the equation for `x`:

```text
x = 2(c + y) + 3b + 4c
x = 2y + 6c + 3b
x - 2y = 3(2c + b)
```

Therefore, we need:

```text
x >= 2y
(x - 2y) % 3 == 0
```

### Case 2: `y < 0`

Since:

```text
c = a - y
```

Substituting:

```text
x = 2a + 3b + 4(a - y)
x = 6a + 3b - 4y
x + 4y = 3(2a + b)
```

Therefore, we need:

```text
x >= -4y
(x + 4y) % 3 == 0
```

## Python Solution

```python
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if y >= 0:
        if x >= 2 * y and (x - 2 * y) % 3 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if x >= -4 * y and (x + 4 * y) % 3 == 0:
            print("YES")
        else:
            print("NO")
```

## Complexity

* **Time:** `O(t)`
* **Space:** `O(1)`

## Example

### Input

```text
11
2 1
3 0
4 -1
4 1
14 1
1 -4
3 -1
2 10
24 -1
24 -3
8 4
```

### Output

```text
YES
YES
YES
NO
YES
NO
NO
NO
NO
YES
YES
```

## Key Takeaway

The important idea is to count how the three allowed moves affect `x` and `y`, then use the relationship between the number of upward and downward moves to derive a simple mathematical condition.
